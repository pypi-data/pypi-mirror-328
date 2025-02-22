import pytest
import yaml

from truefoundry.deploy import Service
from truefoundry.pydantic_v1 import ValidationError


def test_parse_valid_service_spec() -> None:
    """
    Test the Service class for parsing a valid service spec
    """
    spec = """\
name: service
type: service
image:
  type: build
  build_source:
    type: local
  build_spec:
    type: tfy-python-buildpack
    build_context_path: ./
    command: uvicorn main:app --port 4000 --host 0.0.0.0
    pip_packages:
      - fastapi
      - uvicorn
    python_version: '3.11'
ports:
  - expose: true
    host: example.com
    port: 4000
replicas: 2
resources:
  cpu_limit: 0.5
  cpu_request: 0.2
  memory_limit: 512
  memory_request: 256
"""
    service = Service.parse_obj(yaml.safe_load(spec))
    assert service.name == "service"


def test_parse_invalid_service_spec() -> None:
    """
    Test the Service class for parsing a invalid service spec
    """
    spec = """\
name: some-really-long-long-long-long-service-name
type: service
image:
  type: build
  build_source:
    type: local
  build_spec:
    type: tfy-python-buildpack
    build_context_path: ./
    command: uvicorn main:app --port 4000 --host 0.0.0.0
    pip_packages:
      - fastapi
      - uvicorn
    python_version: '3.11'
ports: []
replicas: -1
resources:
  cpu_limit: 0.5
  cpu_request: 0.2
  memory_limit: 512
  memory_request: 256
"""
    with pytest.raises(ValidationError):
        Service.parse_obj(yaml.safe_load(spec))
