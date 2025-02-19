from enum import Enum
from typing import List, Optional, Tuple

GPULocation = Tuple[Optional[str], int]  # (node_ip, gpu_id)
ResourceMapping = List[GPULocation]
ReplicaResourceMapping = List[ResourceMapping]  # List ResourceMapping for each replica


class SchedulerType(Enum):
    FCFS_FIXED_CHUNK = "FCFS_FIXED_CHUNK"
    FCFS = "FCFS"
    EDF = "EDF"
    LRS = "LRS"
    ST = "ST"


class RequestGeneratorType(Enum):
    SYNTHETIC = "SYNTHETIC"
    TRACE = "TRACE"


class RequestIntervalGeneratorType(Enum):
    POISSON = "POISSON"
    GAMMA = "GAMMA"
    STATIC = "STATIC"
    TRACE = "TRACE"


class RequestLengthGeneratorType(Enum):
    UNIFORM = "UNIFORM"
    ZIPF = "ZIPF"
    TRACE = "TRACE"
    FIXED = "FIXED"
