# To be run locally
# Note: This uses a bunch of internal functions for cleanup which are not exposed
import argparse
import copy
import os
import tempfile
import traceback
from typing import TYPE_CHECKING

import coolname
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image
import plotly.express as px
import seaborn as sns
from rich import print
from sklearn.metrics import ConfusionMatrixDisplay

from truefoundry import login
from truefoundry.ml import (
    ArtifactPath,
    BlobStorageDirectory,
    DataDirectoryPath,
    Image,
    LibraryName,
    ModelFramework,
    ONNXFramework,
    PyTorchFramework,
    SpaCyFramework,
    TransformersFramework,
    get_client,
)
from truefoundry.ml.autogen.client import ExperimentIdRequestDto
from truefoundry.ml.session import ACTIVE_RUNS

if TYPE_CHECKING:
    from truefoundry.ml.mlfoundry_api import MlFoundry
    from truefoundry.ml.mlfoundry_run import MlFoundryRun


class CreateMLRepo:
    def __init__(
        self, client: "MlFoundry", ml_repo_name: str, storage_integration_fqn: str
    ) -> None:
        self.client = client
        self.ml_repo_name = ml_repo_name
        self.storage_integration_fqn = storage_integration_fqn
        self._id = None

    def __enter__(self):
        print(f"[yellow]Creating ML repo with name {self.ml_repo_name}")
        self.client.create_ml_repo(
            name=self.ml_repo_name,
            description="End to End CLI Testing ML Repo",
            storage_integration_fqn=self.storage_integration_fqn,
        )
        self._id = self.client._get_ml_repo_id(ml_repo=self.ml_repo_name)

    def __exit__(self, exc_type, exc_val, exc_tb):
        ACTIVE_RUNS.close_active_runs()
        if self._id is not None:
            print(f"[yellow]Deleting ML repo with name {self.ml_repo_name}")
            self.client._experiments_api.hard_delete_experiment_post(
                experiment_id_request_dto=ExperimentIdRequestDto(
                    experiment_id=str(self._id)
                )
            )
            print(f"[yellow]Done deleting ML repo with name {self.ml_repo_name}")


ARTIFACT_NAME = "my-artifact"
MODEL_NAME = "my-model"
EXTERNAL_MODEL_NAME = "my-model-external"
TEST_VERSION_ALIAS_1 = "v1.0.0-test"
TEST_VERSION_ALIAS_2 = "v1.0.1-test"
THIS_DIR = os.path.dirname(os.path.abspath(__file__))


def _compare_file_trees(source: str, target: str):
    for root, _, files in os.walk(source):
        for file in files:
            file1 = os.path.join(root, file)
            file2 = os.path.join(target, os.path.relpath(file1, source))
            assert os.path.exists(file2)


def test_artifact_crud(client: "MlFoundry", ml_repo_name: str):
    print("[yellow]Logging a new artifact (log_artifact) ...")
    artifact_version_1_desc = "This is a sample artifact"
    artifact_version_1_metadata = {
        "created_by": ["truefoundry"],
        "loss": 1.0,
        "epochs": 10,
    }
    artifact_version_1 = client.log_artifact(
        ml_repo=ml_repo_name,
        name=ARTIFACT_NAME,
        artifact_paths=[
            ArtifactPath(src=os.path.join(THIS_DIR, "test_artifact"), dest="some-dir"),
        ],
        description=artifact_version_1_desc,
        metadata=artifact_version_1_metadata,
    )

    print("[yellow]Logging another artifact (log_artifact) ...")
    artifact_version_2_desc = "This is a sample artifact"
    artifact_version_2_metadata = {
        "created_by": ["chiragjn"],
        "loss": 2.0,
        "epochs": 5,
    }
    artifact_version_2 = client.log_artifact(
        ml_repo=ml_repo_name,
        name=ARTIFACT_NAME,
        artifact_paths=[
            ArtifactPath(
                src=os.path.join(THIS_DIR, "test_artifact"),
            ),
        ],
        description=artifact_version_2_desc,
        metadata=artifact_version_2_metadata,
    )

    print("[yellow]Test get_artifact_version_by_fqn ...")
    _fetched_artifact_version_1 = client.get_artifact_version_by_fqn(
        fqn=artifact_version_1.fqn
    )
    assert _fetched_artifact_version_1.fqn == artifact_version_1.fqn
    assert (
        _fetched_artifact_version_1.description
        == artifact_version_1.description
        == artifact_version_1_desc
    )
    assert (
        _fetched_artifact_version_1.metadata
        == artifact_version_1.metadata
        == artifact_version_1_metadata
    )

    print("[yellow]Test get_artifact_version ...")
    _fetched_artifact_version_2 = client.get_artifact_version(
        ml_repo=ml_repo_name,
        name=ARTIFACT_NAME,
        version=artifact_version_2.version,
    )
    assert _fetched_artifact_version_2.fqn == artifact_version_2.fqn
    assert (
        _fetched_artifact_version_2.description
        == artifact_version_2.description
        == artifact_version_2_desc
    )
    assert (
        _fetched_artifact_version_2.metadata
        == artifact_version_2.metadata
        == artifact_version_2_metadata
    )

    print("[yellow]Test list_artifact_versions_by_fqn ...")
    artifact_versions = list(
        client.list_artifact_versions_by_fqn(
            artifact_fqn=artifact_version_1.artifact_fqn
        )
    )
    assert len(artifact_versions) == 2

    print("[yellow]Test list_artifact_versions ...")
    artifact_versions = list(
        client.list_artifact_versions(ml_repo=ml_repo_name, name=ARTIFACT_NAME)
    )
    assert len(artifact_versions) == 2

    print("[yellow]Test artifact_version download ...")
    with tempfile.TemporaryDirectory() as tempdir:
        download_path = artifact_version_1.download(path=tempdir)
        _compare_file_trees(
            source=os.path.join(THIS_DIR, "test_artifact"),
            target=os.path.join(download_path, "some-dir"),
        )

    print("[yellow]Test artifact_version update ...")
    artifact_version_1_updated_desc = "Updated description"
    artifact_version_1.description = artifact_version_1_updated_desc
    artifact_version_1.metadata["loss"] = 2.0
    artifact_version_1_updated_metadata = copy.deepcopy(artifact_version_1.metadata)
    artifact_version_1.version_alias = TEST_VERSION_ALIAS_1
    artifact_version_1.update()

    _fetched_artifact_version_1 = client.get_artifact_version_by_fqn(
        fqn=artifact_version_1.fqn
    )
    assert _fetched_artifact_version_1.fqn == artifact_version_1.fqn
    assert (
        _fetched_artifact_version_1.description
        == artifact_version_1.description
        == artifact_version_1_updated_desc
    )
    assert (
        _fetched_artifact_version_1.metadata
        == artifact_version_1.metadata
        == artifact_version_1_updated_metadata
    )
    assert (
        _fetched_artifact_version_1.version_alias
        == artifact_version_1.version_alias
        == TEST_VERSION_ALIAS_1
    )

    print("[yellow]Test artifact_version delete ...")
    artifact_version_1.delete()
    artifact_version_2.delete()


def test_model_crud(client: "MlFoundry", ml_repo_name: str):
    print("[yellow]Logging a new model (log_model) ...")
    model_version_1_desc = "This is a sample artifact"
    model_version_1_metadata = {
        "created_by": ["truefoundry"],
        "loss": 1.0,
        "epochs": 10,
    }
    model_version_1 = client.log_model(
        ml_repo=ml_repo_name,
        name=MODEL_NAME,
        model_file_or_folder=os.path.join(THIS_DIR, "test_model"),
        framework=TransformersFramework(
            library_name=LibraryName.diffusers,
            pipeline_tag="text-to-image",
            base_model=None,
        ),
        description=model_version_1_desc,
        metadata=model_version_1_metadata,
    )

    print("[yellow]Logging another model (log_model) ...")
    model_version_2_desc = "This is a sample artifact"
    model_version_2_metadata = {
        "created_by": ["chiragjn"],
        "loss": 2.0,
        "epochs": 5,
    }
    model_version_2 = client.log_model(
        ml_repo=ml_repo_name,
        name=MODEL_NAME,
        model_file_or_folder=os.path.join(THIS_DIR, "test_model", "config.json"),
        framework=None,
        description=model_version_2_desc,
        metadata=model_version_2_metadata,
    )

    print("[yellow]Test get_model_version_by_fqn ...")
    _fetched_model_version_1 = client.get_model_version_by_fqn(fqn=model_version_1.fqn)
    assert _fetched_model_version_1.fqn == model_version_1.fqn
    assert (
        _fetched_model_version_1.description
        == model_version_1.description
        == model_version_1_desc
    )
    assert (
        _fetched_model_version_1.metadata
        == model_version_1.metadata
        == model_version_1_metadata
    )
    assert _fetched_model_version_1.framework is not None
    assert _fetched_model_version_1.framework.type == "transformers"
    assert _fetched_model_version_1.framework.library_name == LibraryName.diffusers
    assert _fetched_model_version_1.framework.pipeline_tag == "text-to-image"
    assert _fetched_model_version_1.framework.base_model is None

    print("[yellow]Test get_model_version ...")
    _fetched_model_version_2 = client.get_model_version(
        ml_repo=ml_repo_name,
        name=MODEL_NAME,
        version=model_version_2.version,
    )
    assert _fetched_model_version_2.fqn == model_version_2.fqn
    assert (
        _fetched_model_version_2.description
        == model_version_2.description
        == model_version_2_desc
    )
    assert (
        _fetched_model_version_2.metadata
        == model_version_2.metadata
        == model_version_2_metadata
    )
    assert _fetched_model_version_2.framework is None

    print("[yellow]Test list_model_versions_by_fqn ...")
    model_versions = list(
        client.list_model_versions_by_fqn(model_fqn=model_version_1.model_fqn)
    )
    assert len(model_versions) == 2

    print("[yellow]Test list_model_versions ...")
    model_versions = list(
        client.list_model_versions(ml_repo=ml_repo_name, name=MODEL_NAME)
    )
    assert len(model_versions) == 2

    print("[yellow]Test model_version download ...")
    with tempfile.TemporaryDirectory() as tempdir:
        download_info = model_version_1.download(path=tempdir)
        _compare_file_trees(
            source=os.path.join(THIS_DIR, "test_model"),
            target=download_info.model_dir,
        )

    print("[yellow]Test model_version update ...")
    model_version_1_updated_desc = "Updated description"
    model_version_1.description = model_version_1_updated_desc
    model_version_1.metadata["loss"] = 2.0
    model_version_1_updated_metadata = copy.deepcopy(model_version_1.metadata)
    model_version_1.framework = ModelFramework.PYTORCH
    model_version_1.version_alias = TEST_VERSION_ALIAS_2
    model_version_1.update()

    _fetched_model_version_1 = client.get_model_version_by_fqn(fqn=model_version_1.fqn)
    assert _fetched_model_version_1.fqn == model_version_1.fqn
    assert (
        _fetched_model_version_1.description
        == model_version_1.description
        == model_version_1_updated_desc
    )
    assert (
        _fetched_model_version_1.metadata
        == model_version_1.metadata
        == model_version_1_updated_metadata
    )
    assert (
        _fetched_model_version_1.framework
        == model_version_1.framework
        == PyTorchFramework()
    )
    assert (
        _fetched_model_version_1.version_alias
        == model_version_1.version_alias
        == TEST_VERSION_ALIAS_2
    )

    print("[yellow]Test model_version update 2 ...")
    model_version_1_updated_desc = "Updated description 2.0"
    model_version_1.description = model_version_1_updated_desc
    model_version_1_updated_metadata = copy.deepcopy(model_version_1.metadata)
    model_version_1.framework = ONNXFramework()
    model_version_1.version_alias = None
    model_version_1.update()

    _fetched_model_version_1 = client.get_model_version_by_fqn(fqn=model_version_1.fqn)
    assert _fetched_model_version_1.fqn == model_version_1.fqn
    assert (
        _fetched_model_version_1.description
        == model_version_1.description
        == model_version_1_updated_desc
    )
    assert (
        _fetched_model_version_1.metadata
        == model_version_1.metadata
        == model_version_1_updated_metadata
    )
    assert (
        _fetched_model_version_1.framework
        == model_version_1.framework
        == ONNXFramework()
    )
    assert _fetched_model_version_1.version_alias is None

    print("[yellow]Test model_version update 3 ...")
    model_version_1_updated_desc = "Updated description 3.0"
    model_version_1.description = model_version_1_updated_desc
    model_version_1_updated_metadata = copy.deepcopy(model_version_1.metadata)
    model_version_1.framework = None
    model_version_1.version_alias = TEST_VERSION_ALIAS_1
    model_version_1.update()

    _fetched_model_version_1 = client.get_model_version_by_fqn(fqn=model_version_1.fqn)
    assert _fetched_model_version_1.fqn == model_version_1.fqn
    assert (
        _fetched_model_version_1.description
        == model_version_1.description
        == model_version_1_updated_desc
    )
    assert (
        _fetched_model_version_1.metadata
        == model_version_1.metadata
        == model_version_1_updated_metadata
    )
    assert _fetched_model_version_1.framework is None
    assert model_version_1.framework is None
    assert (
        _fetched_model_version_1.version_alias
        == model_version_1.version_alias
        == TEST_VERSION_ALIAS_1
    )

    print("[yellow]Test model_version external source ...")
    # Treat this artifact as an external source and log it as a model
    source_uri = _fetched_model_version_1._model_version.artifact_storage_root
    model_version_external_desc = "This is a sample artifact"
    model_version_external_metadata = {"source_type": "external"}
    model_version_external = client.log_model(
        ml_repo=ml_repo_name,
        name=EXTERNAL_MODEL_NAME,
        model_file_or_folder=BlobStorageDirectory(
            uri=source_uri,
        ),
        framework=ModelFramework.SPACY,
        description=model_version_external_desc,
        metadata=model_version_external_metadata,
    )

    _fetched_model_version_1 = client.get_model_version_by_fqn(
        fqn=model_version_external.fqn
    )
    assert _fetched_model_version_1.fqn == model_version_external.fqn
    assert (
        _fetched_model_version_1.description
        == model_version_external.description
        == model_version_external_desc
    )
    assert (
        _fetched_model_version_1.metadata
        == model_version_external.metadata
        == model_version_external_metadata
    )
    assert (
        _fetched_model_version_1.framework
        == model_version_external.framework
        == SpaCyFramework()
    )
    print("[yellow]Test model_version external source download ...")
    with tempfile.TemporaryDirectory() as tempdir:
        download_info = model_version_external.download(path=tempdir)
        _compare_file_trees(
            source=os.path.join(THIS_DIR, "test_model"),
            target=download_info.model_dir,
        )
        assert os.path.exists(os.path.join(download_info.model_dir, "config.json"))

    print("[yellow]Test model_version delete ...")
    model_version_1.delete()
    model_version_2.delete()
    model_version_external.delete()


def test_data_directory_crud(client: "MlFoundry", ml_repo_name: str):
    print("[yellow]Creating a new data directory (create_data_directory) ...")
    data_directory_1_desc = "This is a sample data directory"
    data_directory_1_metadata = {
        "created_by": ["truefoundry"],
        "loss": 1.0,
        "epochs": 10,
    }
    data_directory_1 = client.create_data_directory(
        name="my-data-dir-1",
        ml_repo=ml_repo_name,
        description=data_directory_1_desc,
        metadata=data_directory_1_metadata,
    )

    print("[yellow]Creating another data directory (create_data_directory) ...")
    data_directory_2_desc = "This is a sample data directory"
    data_directory_2_metadata = {
        "created_by": ["chiragjn"],
        "loss": 2.0,
        "epochs": 5,
    }
    data_directory_2 = client.create_data_directory(
        name="my-data-dir-2",
        ml_repo=ml_repo_name,
        description=data_directory_2_desc,
        metadata=data_directory_2_metadata,
    )

    print("[yellow]Test get_data_directory_by_fqn ...")
    _fetched_data_directory = client.get_data_directory_by_fqn(fqn=data_directory_1.fqn)
    assert _fetched_data_directory.fqn == data_directory_1.fqn
    assert (
        _fetched_data_directory.description
        == data_directory_1.description
        == data_directory_1_desc
    )
    assert (
        _fetched_data_directory.metadata
        == data_directory_1.metadata
        == data_directory_1_metadata
    )

    print("[yellow]Test get_data_directory ...")
    _fetched_data_directory = client.get_data_directory(
        ml_repo=ml_repo_name,
        name="my-data-dir-2",
    )
    assert _fetched_data_directory.fqn == data_directory_2.fqn
    assert (
        _fetched_data_directory.description
        == data_directory_2.description
        == data_directory_2_desc
    )
    assert (
        _fetched_data_directory.metadata
        == data_directory_2.metadata
        == data_directory_2_metadata
    )

    print("[yellow]Test list_data_directories ...")
    data_directories = list(
        client.list_data_directories(
            ml_repo=ml_repo_name,
        )
    )
    assert len(data_directories) == 2

    print("[yellow]Test data_directory add_files ...")
    data_directory_1.add_files(
        file_paths=[
            DataDirectoryPath(
                src=os.path.join(THIS_DIR, "test_data_directory"),
                dest=None,
            ),
        ]
    )

    print("[yellow]Test data_directory list_files ...")
    files = list(data_directory_1.list_files(path="folder1/"))
    assert len(files) == 1
    assert files[0].path == "folder1/file4.txt"

    print("[yellow]Test data_directory download ...")
    with tempfile.TemporaryDirectory() as tempdir:
        download_path = data_directory_1.download(path=tempdir)
        _compare_file_trees(
            source=os.path.join(THIS_DIR, "test_data_directory"),
            target=download_path,
        )

    print("[yellow]Test data_directory update ...")
    data_directory_1_updated_desc = "Updated description"
    data_directory_1.description = data_directory_1_updated_desc
    data_directory_1.metadata["loss"] = 2.0
    data_directory_1_updated_metadata = copy.deepcopy(data_directory_1.metadata)
    data_directory_1.update()

    _fetched_data_directory = client.get_data_directory_by_fqn(fqn=data_directory_1.fqn)
    assert _fetched_data_directory.fqn == data_directory_1.fqn
    assert (
        _fetched_data_directory.description
        == data_directory_1.description
        == data_directory_1_updated_desc
    )
    assert (
        _fetched_data_directory.metadata
        == data_directory_1.metadata
        == data_directory_1_updated_metadata
    )

    print("[yellow]Test data_directory delete ...")
    data_directory_1.delete()
    data_directory_2.delete()


def test_multipart_upload(client: "MlFoundry", ml_repo_name: str):
    with tempfile.TemporaryDirectory() as tempdir:
        model_file = os.path.join(tempdir, "random.dat")
        with open(model_file, "wb") as output:
            output.write(np.random.bytes(100 * 1024 * 1024))
        print("[yellow]Multipart - Logging a new model (log_model) ...")
        model_version = client.log_model(
            ml_repo=ml_repo_name,
            name="large-model",
            model_file_or_folder=model_file,
            framework=ModelFramework.TRANSFORMERS,
            description="This is a large model mean for testing multipart upload",
            metadata={"created_by": ["truefoundry"], "loss": 1.0, "epochs": 10},
            progress=False,
        )
    print("[yellow]Multipart - Test model_version download ...")
    with tempfile.TemporaryDirectory() as tempdir:
        download_info = model_version.download(path=tempdir, progress=False)
        assert os.path.exists(os.path.join(download_info.model_dir, "random.dat"))

    print("[yellow]Multipart - Test model_version delete ...")
    model_version.delete()


def _log_matplotlib_plot(run: "MlFoundryRun", step=10):
    ConfusionMatrixDisplay.from_predictions(["spam", "ham"], ["ham", "ham"])
    run.log_plots({"confusion_matrix": plt}, step=step)
    plt.clf()


def _log_seaborn_plot(run: "MlFoundryRun", step=10):
    sns.set_theme(style="ticks", palette="pastel")
    tips = sns.load_dataset("tips")
    sns.boxplot(x="day", y="total_bill", hue="smoker", palette=["m", "g"], data=tips)
    sns.despine(offset=10, trim=True)
    run.log_plots({"seaborn": plt}, step=step)
    plt.clf()


def _log_plotly_plot(run: "MlFoundryRun", step=10):
    df = px.data.tips()
    fig = px.histogram(
        df,
        x="total_bill",
        y="tip",
        color="sex",
        marginal="rug",
        hover_data=df.columns,
    )
    run.log_plots({"plotly": fig}, step=step)


def test_run_crud(client: "MlFoundry", ml_repo_name: str):
    print("[yellow]Creating a new run (create_run) ...")
    run_1 = client.create_run(
        ml_repo=ml_repo_name, tags={"env": "development", "task": "test"}
    )

    print("[yellow]Creating another run (create_run) ...")
    run_2 = client.create_run(ml_repo=ml_repo_name, run="another-test-run")

    print("[yellow]Test get_run_by_id ...")
    run_by_id = client.get_run_by_id(run_id=run_1.run_id)
    assert run_by_id.run_name == run_1.run_name

    print("[yellow]Test get_run_by_fqn ...")
    run_by_fqn = client.get_run_by_fqn(run_fqn=run_2.fqn)
    assert run_by_fqn.run_name == run_2.run_name

    print("[yellow]Test get_run_by_name ...")
    run_by_name = client.get_run_by_name(ml_repo=ml_repo_name, run_name=run_1.run_name)
    assert run_by_name.run_name == run_1.run_name

    print(
        "[yellow]Searching for runs based on a filter and order criteria (search_runs) ..."
    )
    runs = list(
        client.search_runs(
            ml_repo=ml_repo_name,
            filter_string="tags.env = 'development'",
        )
    )
    assert len(runs) == 1
    assert runs[0].run_name == run_1.run_name

    print("[yellow]Test set_tags + get_tags ...")
    run_1.set_tags({"env": "production", "task": "test"})
    _fetched_tags = run_1.get_tags(no_cache=True)
    assert "env" in _fetched_tags
    assert _fetched_tags["env"] == "production"
    assert "task" in _fetched_tags
    assert _fetched_tags["task"] == "test"

    print("[yellow]Test log_params + get_params ...")
    run_1.log_params({"epochs": 10, "learning_rate": "0.001"})
    assert run_1.get_params(no_cache=True) == {"epochs": "10", "learning_rate": "0.001"}

    print("[yellow]Test log_metrics + get_metrics ...")
    run_1.log_metrics({"accuracy": 0.5, "loss": 0.9})
    run_1.log_metrics({"accuracy": 0.8, "loss": 0.4}, step=1)
    _fetched_metrics = run_1.get_metrics(metric_names=["accuracy"])
    assert "accuracy" in _fetched_metrics
    assert len(_fetched_metrics["accuracy"]) == 2
    assert [(m.step, m.value) for m in _fetched_metrics["accuracy"]] == [
        (0, 0.5),
        (1, 0.8),
    ]

    # Create and save an image to log.
    print("[yellow]Test log_images ...")
    imarray = np.random.randint(low=0, high=256, size=(100, 100, 3))
    im = PIL.Image.fromarray(imarray.astype("uint8")).convert("RGB")
    with tempfile.TemporaryDirectory() as tempdir:
        img_path = os.path.join(tempdir, "result_image.jpeg")
        im.save(img_path)
        # Log images using different methods of specifying the image source.
        images_to_log = {
            "logged-image-array": Image(data_or_path=imarray),
            "logged-pil-image": Image(data_or_path=im),
            "logged-image-from-path": Image(data_or_path=img_path),
        }
        run_1.log_images(images_to_log, step=100)
    _fetched_images = list(run_1.list_artifact_versions(artifact_type="image"))
    assert len(_fetched_images) == 3

    # Log plots using different plotting libraries.
    print("[yellow]Test log_plots ...")
    _log_matplotlib_plot(run_1, step=10)
    _log_seaborn_plot(run_1, step=1000)
    _log_plotly_plot(run_1, step=100)
    _fetched_plots = list(run_1.list_artifact_versions(artifact_type="plot"))
    assert len(_fetched_plots) == 3

    print("[yellow]Logging a new artifact (log_artifact) ...")
    artifact_version_1 = run_1.log_artifact(
        name=ARTIFACT_NAME,
        artifact_paths=[
            ArtifactPath(src=os.path.join(THIS_DIR, "test_artifact"), dest="some-dir"),
        ],
        description="This is a sample artifact",
        metadata={"created_by": ["truefoundry"], "loss": 1.0, "epochs": 10},
        step=50,
    )
    print("[yellow]Test list_artifact_versions ...")
    _fetched_artifact_versions = list(
        run_1.list_artifact_versions(artifact_type="artifact")
    )
    assert len(_fetched_artifact_versions) == 1
    assert _fetched_artifact_versions[0].fqn == artifact_version_1.fqn

    print("[yellow]Logging a new model (log_model) ...")
    model_version_1 = run_1.log_model(
        name=MODEL_NAME,
        model_file_or_folder=os.path.join(THIS_DIR, "test_model"),
        framework=ModelFramework.TRANSFORMERS,
        description="This is a sample artifact",
        metadata={"created_by": ["truefoundry"], "loss": 1.0, "epochs": 10},
        step=150,
    )
    print("[yellow]Test list_model_versions ...")
    _fetched_model_versions = list(run_1.list_model_versions())
    assert len(_fetched_model_versions) == 1
    assert _fetched_model_versions[0].fqn == model_version_1.fqn
    assert _fetched_model_versions[0].framework is not None
    assert _fetched_model_versions[0].framework.type == "transformers"

    print("[yellow]Test end on run ...")
    run_1.end()

    print("[yellow]Test delete on run ...")
    run_1.delete()


def main(host: str, storage_integration_fqn: str):
    print("[yellow]Call Login ...")
    login(host=host)

    # Initialize the MLFoundry client.
    print("[yellow]Call get_client ...")
    client = get_client()

    # Generate a random ML repository name and print it.
    ml_repo_name = f"test-{os.getpid()}-" + coolname.generate_slug(4)
    print("[yellow]Test create_ml_repo ...")
    with CreateMLRepo(
        client=client,
        ml_repo_name=ml_repo_name,
        storage_integration_fqn=storage_integration_fqn,
    ):
        # Create a new run in the ML repository.
        print("[yellow]Listing all ML Repos (list_ml_repos) ...")
        repos = client.list_ml_repos()
        assert ml_repo_name in repos

        test_run_crud(client=client, ml_repo_name=ml_repo_name)
        test_artifact_crud(client=client, ml_repo_name=ml_repo_name)
        test_model_crud(client=client, ml_repo_name=ml_repo_name)
        test_data_directory_crud(client=client, ml_repo_name=ml_repo_name)
        test_multipart_upload(client=client, ml_repo_name=ml_repo_name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--host",
        type=str,
        default="https://internal.devtest.truefoundry.tech",
    )
    parser.add_argument(
        "--storage-integration-fqn",
        type=str,
        default="truefoundry:aws:tfy-usea1-ctl-devtest-internal:blob-storage:blob",
    )
    parser.add_argument(
        "--with-debugger",
        action="store_true",
        default=False,
    )
    args = parser.parse_args()
    try:
        main(host=args.host, storage_integration_fqn=args.storage_integration_fqn)
    except Exception as e:
        if args.with_debugger:
            pdb = __import__("pdb")
            print(traceback.format_exc())
            print("[red]Exception occurred, starting debugger ...")
            pdb.post_mortem()
        raise e
