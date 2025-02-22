import os
from dataclasses import dataclass
from pathlib import Path

import pytest
import yaml
from click.testing import CliRunner

from tests.itest.utils import (
    ITEST_EXAMPLES_DIR,
    clean_cli_output,
    modify_name_in_manifest_file,
    override_field_in_yaml_file,
)
from truefoundry.cli.__main__ import create_truefoundry_cli

runner = CliRunner()


@dataclass
class DeployTestState:
    """Manages state for deployment tests"""

    workspace_yaml_path: Path = (
        Path(ITEST_EXAMPLES_DIR) / "deploy/internal_workspace.yaml"
    )
    workspace_yaml: dict = None
    workspace_name: str = ""
    workspace_fqn: str = ""
    cluster_fqn: str = ""

    def __post_init__(self):
        self._set_cluster_fqn()
        self._initialize_workspace()

    def _set_cluster_fqn(self):
        """Set cluster_fqn from environment variable"""
        self.cluster_fqn = os.getenv("ITEST_CLUSTER_FQN")
        if not self.cluster_fqn:
            raise ValueError("ITEST_CLUSTER_FQN environment variable is required")
        override_field_in_yaml_file(
            self.workspace_yaml_path,
            "cluster_fqn",
            self.cluster_fqn,
        )

    def _initialize_workspace(self):
        """Initialize workspace with unique name"""
        # There might be other workspaces in the cluster with the same name (failed tests or coincidence)
        # So we need to modify the workspace name to make it unique
        modify_name_in_manifest_file(self.workspace_yaml_path, "itest-internal-ws")
        with open(self.workspace_yaml_path) as f:
            self.workspace_yaml = yaml.safe_load(f)
            self.workspace_name = self.workspace_yaml["name"]
            self.workspace_fqn = (
                f"{self.workspace_yaml['cluster_fqn']}:{self.workspace_name}"
            )


@pytest.fixture(scope="session", autouse=True)
def cli_setup():
    """Primary setup fixture for CLI authentication. Runs automatically for all tests."""
    # Get TFY host and API key from environment variable
    tfy_host = os.getenv("ITEST_TFY_HOST")
    tfy_api_key = os.getenv("ITEST_TFY_API_KEY")
    if not tfy_host or not tfy_api_key:
        raise ValueError(
            "ITEST_TFY_HOST and ITEST_TFY_API_KEY environment variables are required"
        )

    print("\n----- CLI Setup -----")
    result = runner.invoke(
        create_truefoundry_cli(),
        ["login", "--host", tfy_host, "--api-key", tfy_api_key],
    )
    assert result.exit_code == 0, "CLI login failed"
    yield
    print("----- CLI Cleanup -----")


@pytest.fixture(scope="session")
def deploy_state():
    """Initialize deployment test state"""
    print("\n----- Initializing Deploy Test State -----")
    return DeployTestState()


@pytest.fixture(scope="session")
def workspace_setup(deploy_state):
    """Setup workspace for deployment tests"""
    print("----- Workspace Setup -----")

    # Create workspace
    result = runner.invoke(
        create_truefoundry_cli(), ["apply", "--file", deploy_state.workspace_yaml_path]
    )
    clean_output = clean_cli_output(result.output)
    print(f"Workspace creation output: {clean_output}")
    assert result.exit_code == 0
    assert (
        f"Successfully configured manifest {deploy_state.workspace_name} of type workspace"
        in clean_output
    )

    yield deploy_state

    # Cleanup workspace
    print(f"\n----- Cleaning up workspace: {deploy_state.workspace_name} -----")
    result = runner.invoke(
        create_truefoundry_cli(),
        ["delete", "workspace", "--workspace-fqn", deploy_state.workspace_fqn, "--yes"],
    )
    assert result.exit_code == 0


def pytest_configure(config):
    """Register custom markers."""
    config.addinivalue_line("markers", "integration: mark test as an integration test")
