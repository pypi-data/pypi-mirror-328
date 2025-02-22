import re
import subprocess
import tempfile
import uuid

import yaml

ITEST_EXAMPLES_DIR = "tests/itest/examples"


def clean_cli_output(output: str) -> str:
    """Remove ANSI escape sequences from CLI output"""
    return re.sub(r"\x1b\[[0-9;]*[a-zA-Z]", "", output)


def execute_python_script(script: str, timeout: float = 60) -> str:
    """
    Execute a Python script and return the output

    Args:
        script: The Python script to execute
        timeout: The timeout for the script execution
    """
    try:
        with tempfile.NamedTemporaryFile(mode="w", suffix=".py") as f:
            f.write(script)
            f.flush()

            # Run the script and capture output
            result = subprocess.run(
                ["python", f.name],
                check=True,
                capture_output=True,
                text=True,
                timeout=timeout,
            )

            return result.stdout + result.stderr

    except Exception as e:
        print(f"Unexpected error during script execution: {str(e)}")
        raise


def modify_name_in_manifest_file(manifest_path: str, prefix: str) -> None:
    """
    Modify the name in a manifest to make it unique

    Args:
        manifest_path: The path to the manifest file to modify
        prefix: The prefix to add to the new name
    """
    with open(manifest_path) as f:
        manifest = yaml.safe_load(f)
        old_name = manifest["name"]
        new_name = f"{prefix}-{str(uuid.uuid4())[:4]}"
        manifest["name"] = new_name
        if "ports" in manifest:
            for port in manifest["ports"]:
                port["host"] = port["host"].replace(old_name, new_name)
        with open(manifest_path, "w") as f:
            yaml.dump(manifest, f)


def override_field_in_yaml_file(yaml_file, field_name, field_value):
    with open(yaml_file) as f:
        yaml_data = yaml.safe_load(f)
        yaml_data[field_name] = field_value
        with open(yaml_file, "w") as f:
            yaml.dump(yaml_data, f)
