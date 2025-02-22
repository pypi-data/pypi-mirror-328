import glob
import os
import shutil
import uuid
from pprint import pprint

import pytest
import yaml
from click.testing import CliRunner

from tests.itest.utils import (
    ITEST_EXAMPLES_DIR,
    clean_cli_output,
    execute_python_script,
    modify_name_in_manifest_file,
)
from truefoundry.cli.__main__ import create_truefoundry_cli
from truefoundry.deploy.python_deploy_codegen import convert_deployment_config_to_python

runner = CliRunner()


@pytest.mark.integration
class TestDeployCommands:
    """Tests for deployment commands"""

    def _verify_yaml_deployment(self, yaml_file: str, prefix: str, deploy_state):
        """Verify deployment using YAML configuration"""
        src_dir = os.path.abspath(os.path.dirname(yaml_file))
        with runner.isolated_filesystem() as temp_dir:
            shutil.copytree(src_dir, temp_dir, dirs_exist_ok=True)
            yaml_file = os.path.join(temp_dir, os.path.basename(yaml_file))
            modify_name_in_manifest_file(yaml_file, prefix)
            with open(yaml_file) as f:
                yaml_contents = yaml.safe_load(f)
                result = runner.invoke(
                    create_truefoundry_cli(),
                    [
                        "deploy",
                        "--file",
                        yaml_file,
                        "--workspace-fqn",
                        deploy_state.workspace_fqn,
                        "--no-wait",
                    ],
                )
                clean_output = clean_cli_output(result.output)
                pprint(f"Clean output: {clean_output}")
                assert result.exit_code == 0
                assert "🚀 Deployment started for application" in clean_output
                assert f"'{yaml_contents['name']}'" in clean_output

    def _verify_python_deployment(self, yaml_file: str, prefix: str, deploy_state):
        """Verify deployment using Python configuration"""
        src_dir = os.path.abspath(os.path.dirname(yaml_file))
        with runner.isolated_filesystem() as temp_dir:
            shutil.copytree(src_dir, temp_dir, dirs_exist_ok=True)
            yaml_file = os.path.join(temp_dir, os.path.basename(yaml_file))
            modify_name_in_manifest_file(yaml_file, prefix)
            with open(yaml_file) as f:
                yaml_contents = yaml.safe_load(f)
                script = convert_deployment_config_to_python(
                    workspace_fqn=deploy_state.workspace_fqn,
                    application_spec=yaml_contents,
                )
                output = execute_python_script(script=script)
                clean_output = clean_cli_output(output)
                pprint(f"Clean output: {clean_output}")
                assert "🚀 Deployment started for application" in clean_output
                assert f"'{yaml_contents['name']}'" in clean_output

    def test_deploy_service(self, workspace_setup):
        """Test service deployment using both YAML and Python configurations"""
        yaml_files = glob.glob(f"{ITEST_EXAMPLES_DIR}/deploy/service/*/tf.yaml")
        for yaml_file in yaml_files:
            # Test YAML deployment
            prefix = f"itest-service-{yaml_file.split('/')[-2]}"
            self._verify_yaml_deployment(yaml_file, prefix, workspace_setup)

            # Test Python deployment
            prefix = f"itest-service-py-{yaml_file.split('/')[-2]}"
            self._verify_python_deployment(yaml_file, prefix, workspace_setup)

    def test_deploy_job(self, workspace_setup):
        """Test job deployment using both YAML and Python configurations"""
        yaml_files = glob.glob(f"{ITEST_EXAMPLES_DIR}/deploy/job/*/tf.yaml")
        for yaml_file in yaml_files:
            # Test YAML deployment
            prefix = f"itest-job-{yaml_file.split('/')[-2]}"
            self._verify_yaml_deployment(yaml_file, prefix, workspace_setup)

            # Test Python deployment
            prefix = f"itest-job-py-{yaml_file.split('/')[-2]}"
            self._verify_python_deployment(yaml_file, prefix, workspace_setup)

    def test_workflow(self, workspace_setup):
        """Test workflow deployment using both YAML and Python configurations"""
        python_files = glob.glob(f"{ITEST_EXAMPLES_DIR}/deploy/workflow/*/workflow.py")
        for python_file in python_files:
            example_name = python_file.split("/")[-2]
            name = f"itest-workflow-{example_name}-{str(uuid.uuid4())[:4]}"
            src_dir = os.path.abspath(os.path.dirname(python_file))
            with runner.isolated_filesystem() as temp_dir:
                shutil.copytree(src_dir, temp_dir, dirs_exist_ok=True)
                python_file = os.path.join(temp_dir, os.path.basename(python_file))
                result = runner.invoke(
                    create_truefoundry_cli(),
                    [
                        "deploy",
                        "workflow",
                        "--name",
                        name,
                        "--file",
                        python_file,
                        "--workspace-fqn",
                        workspace_setup.workspace_fqn,
                    ],
                )
            clean_output = clean_cli_output(result.output)
            pprint(f"Clean output: {clean_output}")
            assert result.exit_code == 0
            assert "🚀 Deployment started for application" in clean_output
            assert f"'{name}'" in clean_output
