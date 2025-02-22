from tempfile import TemporaryDirectory

from truefoundry.common.constants import PythonPackageManager
from truefoundry.deploy import PythonBuild
from truefoundry.deploy.builder.builders.tfy_notebook_buildpack.dockerfile_template import (
    NotebookImageBuild,
)
from truefoundry.deploy.builder.builders.tfy_notebook_buildpack.dockerfile_template import (
    generate_dockerfile_content as tfy_notebook_buildpack_generate_dockerfile_content,
)
from truefoundry.deploy.builder.builders.tfy_python_buildpack.dockerfile_template import (
    generate_dockerfile_content as tfy_python_buildpack_generate_dockerfile_content,
)


def test_python_build_dockerfile_generation_no_deps():
    build_configuration = PythonBuild(
        python_version="3.11",
        requirements_path=None,
        pip_packages=[],
        apt_packages=[],
        command=["python", "main.py"],
    )
    dockerfile_content = tfy_python_buildpack_generate_dockerfile_content(
        build_configuration=build_configuration,
        mount_python_package_manager_conf_secret=True,
    )
    assert dockerfile_content == (
        """
FROM docker.io/truefoundrycloud/test/python:3.11
ENV PATH=/virtualenvs/venv/bin:$PATH
RUN apt update &&     DEBIAN_FRONTEND=noninteractive apt install -y --no-install-recommends git &&     python -m venv /virtualenvs/venv/ &&     rm -rf /var/lib/apt/lists/*

COPY . /app
WORKDIR /app
"""
    )


def test_python_build_dockerfile_generation_no_pip_conf_secret():
    build_configuration = PythonBuild(
        python_version="3.9",
        requirements_path="requirements.txt",
        pip_packages=["numpy<=1.26", "pydantic<2.0", "requests"],
        apt_packages=["libpq-dev", "libjpeg-dev"],
        command=["python", "main.py"],
    )
    dockerfile_content = tfy_python_buildpack_generate_dockerfile_content(
        build_configuration=build_configuration,
        mount_python_package_manager_conf_secret=False,
    )
    assert dockerfile_content == (
        """
FROM docker.io/truefoundrycloud/test/python:3.9
ENV PATH=/virtualenvs/venv/bin:$PATH
RUN apt update &&     DEBIAN_FRONTEND=noninteractive apt install -y --no-install-recommends git &&     python -m venv /virtualenvs/venv/ &&     rm -rf /var/lib/apt/lists/*

RUN apt update && DEBIAN_FRONTEND=noninteractive apt install -y --no-install-recommends libpq-dev libjpeg-dev && rm -rf /var/lib/apt/lists/*
COPY requirements.txt /tmp/requirements.txt
RUN  python -m pip install -U pip setuptools wheel && python -m pip install --use-pep517 --no-cache-dir -r /tmp/requirements.txt 'numpy<=1.26' 'pydantic<2.0' requests
COPY . /app
WORKDIR /app
"""
    )


def test_python_build_dockerfile_generation_with_pip_conf_secret():
    build_configuration = PythonBuild(
        python_version="3.10",
        requirements_path="requirements.txt",
        pip_packages=["numpy<=1.26", "pydantic<2.0", "requests"],
        apt_packages=["libpq-dev", "libjpeg-dev"],
        command=["python", "main.py"],
    )
    dockerfile_content = tfy_python_buildpack_generate_dockerfile_content(
        build_configuration=build_configuration,
        mount_python_package_manager_conf_secret=True,
    )
    assert dockerfile_content == (
        """
FROM docker.io/truefoundrycloud/test/python:3.10
ENV PATH=/virtualenvs/venv/bin:$PATH
RUN apt update &&     DEBIAN_FRONTEND=noninteractive apt install -y --no-install-recommends git &&     python -m venv /virtualenvs/venv/ &&     rm -rf /var/lib/apt/lists/*

RUN apt update && DEBIAN_FRONTEND=noninteractive apt install -y --no-install-recommends libpq-dev libjpeg-dev && rm -rf /var/lib/apt/lists/*
COPY requirements.txt /tmp/requirements.txt
RUN --mount=type=secret,id=pip.conf python -m pip install -U pip setuptools wheel && PIP_CONFIG_FILE=/run/secrets/pip.conf python -m pip install --use-pep517 --no-cache-dir -r /tmp/requirements.txt 'numpy<=1.26' 'pydantic<2.0' requests
COPY . /app
WORKDIR /app
"""
    )


def test_notebook_build_dockerfile_generation_no_build_script():
    build_configuration = NotebookImageBuild(
        base_image_uri="public.ecr.aws/truefoundrycloud/jupyter:0.3.0",
    )
    with TemporaryDirectory() as local_dir:
        dockerfile_content = tfy_notebook_buildpack_generate_dockerfile_content(
            build_configuration=build_configuration,
            local_dir=local_dir,
        )
    assert dockerfile_content == (
        """
FROM public.ecr.aws/truefoundrycloud/jupyter:0.3.0
USER root
USER $NB_UID
"""
    )


def test_notebook_build_dockerfile_generation_with_build_script_and_pip_conf_secret():
    build_configuration = NotebookImageBuild(
        base_image_uri="public.ecr.aws/truefoundrycloud/jupyter:0.3.0",
        build_script="#!/bin/bash\nset -ex\n\nsudo apt install -y curl\n",
    )
    with TemporaryDirectory() as local_dir:
        dockerfile_content = tfy_notebook_buildpack_generate_dockerfile_content(
            build_configuration=build_configuration,
            local_dir=local_dir,
            mount_pip_conf_secret=True,
        )
        assert dockerfile_content == (
            """
FROM public.ecr.aws/truefoundrycloud/jupyter:0.3.0
USER root
COPY build-script-fcd4070fa90ed5f16df55125cb3c156e5970a07fc9c6cd31ccac6e9b2b80bd26.sh /tmp/user-build-script.sh
RUN --mount=type=secret,id=pip.conf mkdir -p /var/log/ && DEBIAN_FRONTEND=noninteractive PIP_CONFIG_FILE=/run/secrets/pip.conf bash -ex /tmp/user-build-script.sh 2>&1 | tee /var/log/user-build-script-output.log && test ${PIPESTATUS[0]} -eq 0

USER $NB_UID
"""
        )


def test_python_build_dockerfile_generation_no_deps_with_uv_package_manager():
    build_configuration = PythonBuild(
        python_version="3.11",
        requirements_path=None,
        pip_packages=[],
        apt_packages=[],
        command=["python", "main.py"],
    )
    dockerfile_content = tfy_python_buildpack_generate_dockerfile_content(
        build_configuration=build_configuration,
        mount_python_package_manager_conf_secret=True,
        package_manager=PythonPackageManager.UV.value,
    )
    assert dockerfile_content == (
        """
FROM docker.io/truefoundrycloud/test/python:3.11
ENV PATH=/virtualenvs/venv/bin:$PATH
RUN apt update &&     DEBIAN_FRONTEND=noninteractive apt install -y --no-install-recommends git &&     python -m venv /virtualenvs/venv/ &&     rm -rf /var/lib/apt/lists/*

COPY . /app
WORKDIR /app
"""
    )


def test_python_build_dockerfile_generation_no_pip_conf_secret_with_uv_package_manager():
    build_configuration = PythonBuild(
        python_version="3.9",
        requirements_path="requirements.txt",
        pip_packages=["numpy<=1.26", "pydantic<2.0", "requests"],
        apt_packages=["libpq-dev", "libjpeg-dev"],
        command=["python", "main.py"],
    )
    dockerfile_content = tfy_python_buildpack_generate_dockerfile_content(
        build_configuration=build_configuration,
        mount_python_package_manager_conf_secret=False,
        package_manager=PythonPackageManager.UV.value,
    )
    assert dockerfile_content == (
        """
FROM docker.io/truefoundrycloud/test/python:3.9
ENV PATH=/virtualenvs/venv/bin:$PATH
RUN apt update &&     DEBIAN_FRONTEND=noninteractive apt install -y --no-install-recommends git &&     python -m venv /virtualenvs/venv/ &&     rm -rf /var/lib/apt/lists/*

RUN apt update && DEBIAN_FRONTEND=noninteractive apt install -y --no-install-recommends libpq-dev libjpeg-dev && rm -rf /var/lib/apt/lists/*
COPY requirements.txt /tmp/requirements.txt
RUN  --mount=from=ghcr.io/astral-sh/uv:latest,source=/uv,target=/usr/local/bin/uv python -m pip install -U pip setuptools wheel && UV_LINK_MODE=copy UV_PYTHON_DOWNLOADS=never UV_INDEX_STRATEGY=unsafe-best-match uv pip install --no-cache-dir -r /tmp/requirements.txt 'numpy<=1.26' 'pydantic<2.0' requests
COPY . /app
WORKDIR /app
"""
    )


def test_python_build_dockerfile_generation_with_pip_conf_secret_with_uv_package_manager():
    build_configuration = PythonBuild(
        python_version="3.10",
        requirements_path="requirements.txt",
        pip_packages=["numpy<=1.26", "pydantic<2.0", "requests"],
        apt_packages=["libpq-dev", "libjpeg-dev"],
        command=["python", "main.py"],
    )
    dockerfile_content = tfy_python_buildpack_generate_dockerfile_content(
        build_configuration=build_configuration,
        mount_python_package_manager_conf_secret=True,
        package_manager=PythonPackageManager.UV.value,
    )
    assert dockerfile_content == (
        """
FROM docker.io/truefoundrycloud/test/python:3.10
ENV PATH=/virtualenvs/venv/bin:$PATH
RUN apt update &&     DEBIAN_FRONTEND=noninteractive apt install -y --no-install-recommends git &&     python -m venv /virtualenvs/venv/ &&     rm -rf /var/lib/apt/lists/*

RUN apt update && DEBIAN_FRONTEND=noninteractive apt install -y --no-install-recommends libpq-dev libjpeg-dev && rm -rf /var/lib/apt/lists/*
COPY requirements.txt /tmp/requirements.txt
RUN --mount=type=secret,id=uv.toml --mount=from=ghcr.io/astral-sh/uv:latest,source=/uv,target=/usr/local/bin/uv python -m pip install -U pip setuptools wheel && UV_LINK_MODE=copy UV_PYTHON_DOWNLOADS=never UV_INDEX_STRATEGY=unsafe-best-match UV_CONFIG_FILE=/run/secrets/uv.toml uv pip install --no-cache-dir -r /tmp/requirements.txt 'numpy<=1.26' 'pydantic<2.0' requests
COPY . /app
WORKDIR /app
"""
    )
