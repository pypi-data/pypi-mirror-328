# Development

## Instructions

Install `uv`

Follow the docs at https://docs.astral.sh/uv/getting-started/installation/


```bash
# git clone
git clone https://github.com/truefoundry/truefoundry-cli
cd truefoundry-cli

# Setup the virtual environment
uv venv --python 3.9  # or any higher python version
uv sync --locked --all-extras --dev

# install pre-commit file formatting hooks
uv run pre-commit install --install-hooks
uv run pre-commit

# run the tests (inside the shell)
uv run pytest
```

# Connecting to Local TFY Services

```
cp .tfy-cli-local.env.example .tfy-cli-local.env
export TFY_CLI_LOCAL_DEV_MODE=1
```

You can control which servicefoundry server and mlfoundry server using the `.tfy-cli-local.env` file

## Releasing a New Version

To release a new version of the TrueFoundry CLI as a Python package, create a new tag on the main branch using GitHub Releases. This will trigger a workflow that publishes the pip package. Tags must be in the format `vx.x.x`, for example `v0.1.0`.


# truefoundry/ml/autogen Notes

- Some of the APIs on backend are not encapsulating the request in a DTO
- It stuffs all entities in truefoundry.ml.autogen.client __init__ which might cause namespace conflicts
- We should have proper MLRepo Entity and some of the methods on Run need to be action oriented
