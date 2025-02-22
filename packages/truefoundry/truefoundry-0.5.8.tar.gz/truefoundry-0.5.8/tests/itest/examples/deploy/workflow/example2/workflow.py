from truefoundry.deploy import Resources
from truefoundry.workflow import (
    FlyteDirectory,
    PythonTaskConfig,
    TaskPythonBuild,
    task,
    workflow,
)

task_config = PythonTaskConfig(
    image=TaskPythonBuild(
        python_version="3.9",
        pip_packages=["truefoundry[workflow]==0.4.7rc0"],
    ),
    resources=Resources(cpu_request=0.45),
    service_account="default",
)


@task(task_config=task_config)
def create_directory() -> FlyteDirectory:
    import os

    dir_path = "/tmp/sample_directory"
    os.makedirs(dir_path, exist_ok=True)

    # Create multiple text files in the directory
    for i in range(3):
        with open(os.path.join(dir_path, f"file_{i}.txt"), "w") as f:
            f.write(f"Content of file {i}\n")

    return FlyteDirectory(dir_path)


@task(task_config=task_config)
def read_and_print_directory(directory: FlyteDirectory) -> str:
    import os

    # List all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        with open(file_path, "r") as f:
            content = f.read()
            print(f"Contents of {filename}:")
            print(content)
    return "Done reading and printing the directory."


@workflow
def simple_directory_workflow():
    directory = create_directory()
    read_and_print_directory(directory=directory)
