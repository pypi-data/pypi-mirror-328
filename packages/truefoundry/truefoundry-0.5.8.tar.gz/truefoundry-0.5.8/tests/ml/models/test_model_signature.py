import numpy as np

from truefoundry.ml.autogen.models import (
    ColSpec,
    ModelSignature,
    Schema,
    TensorSpec,
    infer_signature,
)


def test_infer_signature_numpy() -> None:
    X = np.random.rand(256, 256, 3)
    Y = np.random.rand(512, 512, 3)
    sig = infer_signature(X, Y)
    expected_output = ModelSignature(
        inputs=Schema(
            inputs=[TensorSpec(type=np.dtype(np.float64), shape=(-1, 256, 3))]
        ),
        outputs=Schema(
            inputs=[TensorSpec(type=np.dtype(np.float64), shape=(-1, 512, 3))]
        ),
        params=None,
    )
    assert sig == expected_output, "Signature inference failed for numpy arrays"


def test_infer_signature_dataframe() -> None:
    import pandas as pd

    X = pd.DataFrame(
        {
            "feature_float": [50.0],
            "feature_int": [25],
            "feature_category": ["B"],
            "feature_binary": [True],
        }
    )
    Y = np.array([[5.0, 10.0]])
    sig = infer_signature(X, Y)
    expected_output = ModelSignature(
        inputs=Schema(
            inputs=[
                ColSpec(name="feature_float", type="double", required=True),
                ColSpec(name="feature_int", type="long", required=True),
                ColSpec(name="feature_category", type="string", required=True),
                ColSpec(name="feature_binary", type="boolean", required=True),
            ]
        ),
        outputs=Schema(inputs=[TensorSpec(type=np.dtype(np.float64), shape=(-1, 2))]),
        params=None,
    )
    assert sig == expected_output, "Signature inference failed for pandas DataFrames"
