import os


class GitHubCIConfig:
    """
    Configuration class to manage environment variables and application settings.
    """

    def __init__(self) -> None:
        self.is_ci: bool = bool(os.getenv("GITHUB_RUN_ID"))
        self.run_id: str | int = self._get_env_variable("GITHUB_RUN_ID", default="dev")
        self.run_id = int(self.run_id) if self.is_ci else self.run_id
        self.github_token: str | None = self._get_env_variable(
            "GITHUB_TOKEN", required=self.is_ci
        )
        self.github_sha: str = self._get_env_variable("GITHUB_SHA", default="dev")
        self.github_repository: str = self._get_env_variable(
            "GITHUB_REPOSITORY", default="gatech-sysml/vajra"
        )
        self.repo_owner, self.repo_name = self.github_repository.split("/")
        self.baseline_branch: str = self._get_env_variable(
            "BASELINE_BRANCH", default="main"
        )
        self.workspace: str = self._get_env_variable("WORKSPACE", default=os.getcwd())
        self.output_dir: str = os.path.join(
            self.workspace, "test_output", "performance"
        )
        self.workflow_filename: str = "test_suite"
        self.workflow_name: str = "Test suite"
        self.performance_artifact_prefix: str = "perf_results"
        self.comparison_result_prefix: str = "comparison_results"
        self.regression_threshold_pct: int = (
            2  # minimum % difference between runs to consider as regression
        )

    @staticmethod
    def _get_env_variable(
        var_name: str, required: bool = False, default: str | None = None
    ) -> str | None:
        """
        Helper function to get environment variables with optional required check and default value.
        """
        value: str | None = os.getenv(var_name)
        if required and not value:
            raise EnvironmentError(f"{var_name} environment variable is not set")
        return value if value is not None else default
