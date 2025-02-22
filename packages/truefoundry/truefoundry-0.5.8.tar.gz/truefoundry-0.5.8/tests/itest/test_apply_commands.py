import glob
import os
import shutil
from pprint import pprint

import pytest
import yaml
from click.testing import CliRunner

from tests.itest.api_client import TruefoundryAPIClient
from tests.itest.utils import (
    ITEST_EXAMPLES_DIR,
    clean_cli_output,
    modify_name_in_manifest_file,
    override_field_in_yaml_file,
)
from truefoundry.cli.__main__ import create_truefoundry_cli

runner = CliRunner()


@pytest.mark.integration
class TestApplyCommands:
    """Tests for apply commands"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Fixture to set up API client for all tests"""
        self.tenant_name = os.getenv("ITEST_TENANT_NAME")
        self.cluster_fqn = os.getenv("ITEST_CLUSTER_FQN")
        self.storage_integration_fqn = os.getenv("ITEST_STORAGE_INTEGRATION_FQN")
        self.api_client = TruefoundryAPIClient()
        yield self.api_client

    def _verify_apply_command(self, yaml_file: str, prefix: str):
        """Helper method to verify apply command execution"""
        src_dir = os.path.abspath(os.path.dirname(yaml_file))
        with runner.isolated_filesystem() as temp_dir:
            shutil.copytree(src_dir, temp_dir, dirs_exist_ok=True)
            yaml_file = os.path.join(temp_dir, os.path.basename(yaml_file))
            modify_name_in_manifest_file(yaml_file, prefix)
            override_field_in_yaml_file(yaml_file, "cluster_fqn", self.cluster_fqn)
            with open(yaml_file) as f:
                yaml_contents = yaml.safe_load(f)
                result = runner.invoke(
                    create_truefoundry_cli(),
                    [
                        "apply",
                        "--file",
                        yaml_file,
                    ],
                )
                clean_output = clean_cli_output(result.output)
                pprint(f"Clean output: {clean_output}")
                assert result.exit_code == 0
                assert (
                    f"Successfully configured manifest {yaml_contents['name']}"
                    in clean_output
                )

                # Return the yaml contents for cleanup
                return yaml_contents

    def _delete_workspace(self, workspace_fqn: str):
        """Helper method to delete workspace"""
        result = runner.invoke(
            create_truefoundry_cli(),
            [
                "delete",
                "workspace",
                "--workspace-fqn",
                workspace_fqn,
                "--yes",
            ],
        )
        clean_output = clean_cli_output(result.output)
        assert result.exit_code == 0
        assert f"Deleted workspace '{workspace_fqn}'" in clean_output

    def test_apply_provider_account(self):
        """Test applying provider account configurations"""
        yaml_files = glob.glob(f"{ITEST_EXAMPLES_DIR}/apply/provider_account/*/tf.yaml")
        for yaml_file in yaml_files:
            prefix = f"itest-pa-{yaml_file.split('/')[-2]}"
            yaml_contents = self._verify_apply_command(yaml_file, prefix)
            provider_account_fqn = f"{self.tenant_name}:{yaml_contents['type'].split('/')[-1]}:{yaml_contents['name']}"
            pprint(provider_account_fqn)
            self.api_client.delete_provider_account(provider_account_fqn)

    def test_apply_workspace(self):
        """Test applying workspace configurations"""
        yaml_files = glob.glob(f"{ITEST_EXAMPLES_DIR}/apply/workspace/*/tf.yaml")
        for yaml_file in yaml_files:
            prefix = f"itest-ws-{yaml_file.split('/')[-2]}"
            yaml_contents = self._verify_apply_command(yaml_file, prefix)
            workspace_fqn = f"{yaml_contents['cluster_fqn']}:{yaml_contents['name']}"
            self._delete_workspace(workspace_fqn)

    def test_apply_ml_repo(self):
        """Test applying ML repository configurations"""
        yaml_files = glob.glob(f"{ITEST_EXAMPLES_DIR}/apply/ml_repo/*/tf.yaml")
        for yaml_file in yaml_files:
            override_field_in_yaml_file(
                yaml_file, "storage_integration_fqn", self.storage_integration_fqn
            )
            prefix = f"itest-mlrepo-{yaml_file.split('/')[-2]}"
            yaml_contents = self._verify_apply_command(yaml_file, prefix)
            repo_name = yaml_contents["name"]
            self.api_client.delete_ml_repo(repo_name)
