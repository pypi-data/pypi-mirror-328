import random
from functools import partial

from truefoundry.workflow import (
    PythonTaskConfig,
    TaskPythonBuild,
    conditional,
    map_task,
    task,
    workflow,
)

task_config = PythonTaskConfig(
    image=TaskPythonBuild(
        python_version="3.11",
        pip_packages=["truefoundry[workflow]==0.4.8"],
    )
)


@task(task_config=task_config)
def generate_number() -> int:
    return random.randint(1, 10)


@task(task_config=task_config)
def process_low() -> str:
    return "Low number processing"


@task(task_config=task_config)
def process_high() -> str:
    return "High number processing"


@task(task_config=task_config)
def square(x: int) -> int:
    return x * x


@workflow
def conditional_and_map_workflow(numbers: list[int]) -> str:
    number = generate_number()

    result = (
        conditional("branch")
        .if_(number < 5)
        .then(process_low())
        .else_()
        .then(process_high())
    )

    square_task = partial(square)
    squared_array = map_task(square_task)(x=numbers)
    print(f"Square of {numbers} is {squared_array}")

    return result
