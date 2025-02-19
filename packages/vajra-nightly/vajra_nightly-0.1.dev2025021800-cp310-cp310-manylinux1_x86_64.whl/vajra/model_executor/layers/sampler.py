"""A layer that samples the next tokens from the model's outputs."""

from typing import List, Tuple

import torch
import torch.nn as nn

from vajra._datatypes_C import SequenceMetadata
from vajra.core.datatypes import SamplerOutput, SamplerOutputs, SamplingType, Sequence
from vajra.model_executor.parallel_utils import gather_from_tensor_model_parallel_region

_SAMPLING_EPS = 1e-5


class Sampler(nn.Module):
    """Samples the next tokens from the model's outputs.

    This layer does the following:
    1. Discard the hidden states that are not used for sampling (i.e., all
        tokens except the final one in each prompt).
    2. Compute the logits for the next tokens.
    3. Apply presence and frequency penalties.
    4. Apply temperature scaling.
    5. Apply top-p and top-k truncation.
    6. Sample the next tokens.
    Here, each sequence group within the batch can have different sampling
    parameters (e.g., sampling method, temperature, top-p, top-k, etc.).
    """

    def __init__(self, embedding: torch.Tensor, vocab_size: int) -> None:
        super().__init__()
        self.embedding = embedding
        self.vocab_size = vocab_size

    def forward(
        self,
        logits: torch.Tensor,
        seqs: List[Sequence],
        seq_metadata_list: List[SequenceMetadata],
    ) -> SamplerOutputs:
        # Get the hidden states that we use for sampling.
        logits = _prune_hidden_states(logits, seq_metadata_list)

        # Get the logits for the next tokens.
        logits = _get_logits(logits, self.embedding, self.vocab_size)

        # Apply temperature scaling.
        temperatures = _get_temperatures(seqs)
        if any(t != 1.0 for t in temperatures):
            t = torch.tensor(temperatures, dtype=logits.dtype, device=logits.device)
            # Use in-place division to avoid creating a new tensor.
            logits.div_(t.unsqueeze(dim=1))

        # Apply top-p and top-k truncation.
        top_ps, top_ks = _get_top_p_top_k(seqs, self.vocab_size)
        assert len(top_ps) == len(top_ks) == logits.shape[0]
        do_top_p = any(p < 1.0 - _SAMPLING_EPS for p in top_ps)
        do_top_k = any(k != self.vocab_size for k in top_ks)
        if do_top_p or do_top_k:
            logits = _apply_top_p_top_k(logits, top_ps, top_ks)

        # We use float32 for probabilities and log probabilities.
        # Compute the probabilities.
        probs = torch.softmax(logits, dim=-1, dtype=torch.float)
        # Compute the log probabilities.
        # Use log_softmax to ensure numerical stability.
        logprobs = torch.log_softmax(logits, dim=-1, dtype=torch.float)

        # Sample the next tokens.
        return _sample(probs, logprobs, seqs, seq_metadata_list)


def _get_logits(
    hidden_states: torch.Tensor, embedding: torch.Tensor, vocab_size: int
) -> torch.Tensor:
    # Get the logits for the next tokens.
    logits = torch.matmul(hidden_states, embedding.t())
    logits = gather_from_tensor_model_parallel_region(logits)
    # Remove paddings in vocab (if any).
    logits = logits[:, :vocab_size]
    return logits


def _prune_hidden_states(
    hidden_states: torch.Tensor,
    seq_metadata_list: List[SequenceMetadata],
) -> torch.Tensor:
    last_token_indices = []
    token_idx = 0
    for seq_metadata in seq_metadata_list:
        num_q_tokens = seq_metadata.num_q_tokens
        last_token_indices.append(token_idx + num_q_tokens - 1)
        token_idx += num_q_tokens

    last_token_indices = torch.tensor(
        last_token_indices, dtype=torch.long, device=hidden_states.device
    )
    return hidden_states.index_select(0, last_token_indices)


def _get_temperatures(seqs: List[Sequence]) -> List[float]:
    # Collect the temperatures for the logits.
    temperatures: List[float] = []
    for seq in seqs:
        temperature = seq.sampling_params.temperature
        if temperature < _SAMPLING_EPS:
            # NOTE: Zero temperature means deterministic sampling
            # (i.e., greedy sampling or beam search).
            # Set the temperature to 1 to avoid division by zero.
            temperature = 1.0
        temperatures.append(temperature)
    return temperatures


def _get_top_p_top_k(
    seqs: List[Sequence],
    vocab_size: int,
) -> Tuple[List[float], List[int]]:
    top_ps: List[float] = []
    top_ks: List[int] = []
    for seq in seqs:
        top_p = seq.sampling_params.top_p
        # k should not be greater than the vocab size.
        top_k = min(seq.sampling_params.top_k, vocab_size)
        # k=-1 means no truncation.
        top_k = vocab_size if top_k == -1 else top_k
        top_ps.append(top_p)
        top_ks.append(top_k)
    return top_ps, top_ks


def _apply_top_p_top_k(
    logits: torch.Tensor,
    top_ps: List[float],
    top_ks: List[int],
) -> torch.Tensor:
    p = torch.tensor(top_ps, dtype=logits.dtype, device=logits.device)
    k = torch.tensor(top_ks, dtype=torch.int, device=logits.device)
    logits_sort, logits_idx = logits.sort(dim=-1, descending=True)

    # Apply top-p.
    probs_sort = logits_sort.softmax(dim=-1)
    probs_sum = probs_sort.cumsum(dim=-1)
    top_p_mask = (probs_sum - probs_sort) > p.unsqueeze(dim=1)
    logits_sort[top_p_mask] = -float("inf")

    # Apply top-k.
    # Create a mask for the top-k elements.
    top_k_mask = torch.arange(logits_idx.shape[-1], device=logits_idx.device)
    top_k_mask = top_k_mask.expand(logits_idx.shape[0], -1)
    top_k_mask = top_k_mask >= k.unsqueeze(dim=1)
    logits_sort[top_k_mask] = -float("inf")

    # Re-sort the probabilities.
    logits = torch.gather(logits_sort, dim=-1, index=torch.argsort(logits_idx, dim=-1))
    return logits


def _greedy_sample(
    logprobs: torch.Tensor,
) -> List[Tuple[List[int], List[int]]]:
    return torch.argmax(logprobs, dim=-1).view(-1).cpu().tolist()


def _random_sample(
    probs: torch.Tensor,
) -> List[Tuple[List[int], List[int]]]:
    random_samples = (
        torch.multinomial(probs, num_samples=1, replacement=True)
        .view(-1)
        .cpu()
        .tolist()
    )

    return random_samples


def _sample(
    probs: torch.Tensor,
    logprobs: torch.Tensor,
    seqs: List[Sequence],
    seq_metadata_list: List[SequenceMetadata],
) -> SamplerOutputs:
    categorized_seq_indices = {t: [] for t in SamplingType}
    category_num_tokens = {t: 0 for t in SamplingType}

    for i, seq in enumerate(seqs):
        sampling_type = seq.sampling_params.sampling_type
        categorized_seq_indices[sampling_type].append(i)
        category_num_tokens[sampling_type] += 1

    outputs: List[SamplerOutput] = [None] * len(seq_metadata_list)

    for sampling_type in SamplingType:
        seq_indices = categorized_seq_indices[sampling_type]
        num_tokens = category_num_tokens[sampling_type]
        if num_tokens == 0:
            continue
        category_logprobs = logprobs[seq_indices]
        category_probs = probs[seq_indices]
        if sampling_type == SamplingType.GREEDY:
            sample_results = _greedy_sample(category_logprobs)
        elif sampling_type == SamplingType.RANDOM:
            sample_results = _random_sample(category_probs)
        else:
            raise ValueError(f"Unsupported sampling type: {sampling_type}")

        for seq_idx, sample_result in zip(seq_indices, sample_results):
            seq_id = seq_metadata_list[seq_idx].seq_id
            schedule_id = seq_metadata_list[seq_idx].schedule_id
            outputs[seq_idx] = SamplerOutput(schedule_id, seq_id, sample_result)

    return outputs
