import os
import tempfile
from pathlib import Path

import joblib
import numpy as np
import pytest

from truefoundry.ml.autogen.client import (
    InferMethodName,
    SklearnSerializationFormat,
    XGBoostSerializationFormat,
)
from truefoundry.ml.model_framework import (
    SklearnFramework,
    XGBoostFramework,
    auto_update_model_framework_details,
    sklearn_infer_schema,
    xgboost_infer_schema,
)
from truefoundry.pydantic_v1 import ValidationError


class TestModelFramework:
    def setup_method(self):
        self.sample_model_file = "tests/ml/data/test_model_1.joblib"
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.model_dir = self.tmp_dir.name

    def teardown_method(self):
        self.tmp_dir.cleanup()

    def create_dummy_model_file(self, model_path) -> str:
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        with open(model_path, "wb") as f:
            with open(self.sample_model_file, "rb") as sample_f:
                f.write(sample_f.read())
        return model_path

    def validate_test_cases(self, test_cases):
        # Loop through test cases
        for test_case in test_cases:
            framework = test_case["input"]["framework"]
            model_file_or_folder = test_case["input"]["model_file_or_folder"]
            auto_update_model_framework_details(
                framework=framework, model_file_or_folder=model_file_or_folder
            )
            assert framework.model_filepath == test_case["expected"]["model_filepath"]
            assert (
                framework.serialization_format
                == test_case["expected"]["serialization_format"]
            )

    def test_auto_update_model_framework_details_1(self):
        """
        TestCases: Directory structure:
            - model.joblib
        """
        model_filepath = os.path.join(self.model_dir, "model.joblib")
        self.create_dummy_model_file(model_filepath)
        test_cases = [
            {
                "input": {
                    "framework": SklearnFramework(),
                    "model_file_or_folder": self.model_dir,
                },
                "expected": {
                    "model_filepath": "model.joblib",
                    "serialization_format": SklearnSerializationFormat.JOBLIB,
                },
            },
            {
                "input": {
                    "framework": XGBoostFramework(),
                    "model_file_or_folder": self.model_dir,
                },
                "expected": {
                    "model_filepath": "model.joblib",
                    "serialization_format": XGBoostSerializationFormat.JOBLIB,
                },
            },
            {
                "input": {
                    "framework": SklearnFramework(),
                    "model_file_or_folder": model_filepath,
                },
                "expected": {
                    "model_filepath": "model.joblib",
                    "serialization_format": SklearnSerializationFormat.JOBLIB,
                },
            },
            {
                "input": {
                    "framework": XGBoostFramework(),
                    "model_file_or_folder": model_filepath,
                },
                "expected": {
                    "model_filepath": "model.joblib",
                    "serialization_format": XGBoostSerializationFormat.JOBLIB,
                },
            },
            {
                "input": {
                    "framework": SklearnFramework(model_filepath=model_filepath),
                    "model_file_or_folder": self.model_dir,
                },
                "expected": {
                    "model_filepath": "model.joblib",
                    "serialization_format": SklearnSerializationFormat.JOBLIB,
                },
            },
            {
                "input": {
                    "framework": XGBoostFramework(model_filepath=model_filepath),
                    "model_file_or_folder": self.model_dir,
                },
                "expected": {
                    "model_filepath": "model.joblib",
                    "serialization_format": XGBoostSerializationFormat.JOBLIB,
                },
            },
        ]
        self.validate_test_cases(test_cases)

    def test_auto_update_model_framework_details_2(self):
        """
        TestCases: Directory structure:
            - model_1.joblib
            - dummy.txt
        """
        model_relative_path = "model_1.joblib"
        model_filepath = os.path.join(self.model_dir, model_relative_path)
        self.create_dummy_model_file(model_filepath)
        txt_file = os.path.join(self.model_dir, "dummy.txt")
        with open(txt_file, "w") as f:
            f.write("dummy text")

        test_cases = [
            {
                "input": {
                    "framework": SklearnFramework(),
                    "model_file_or_folder": self.model_dir,
                },
                "expected": {
                    "model_filepath": None,
                    "serialization_format": None,
                },
            },
            {
                "input": {
                    "framework": XGBoostFramework(),
                    "model_file_or_folder": self.model_dir,
                },
                "expected": {
                    "model_filepath": None,
                    "serialization_format": None,
                },
            },
            {
                "input": {
                    "framework": SklearnFramework(model_filepath=model_relative_path),
                    "model_file_or_folder": model_filepath,
                },
                "expected": {
                    "model_filepath": model_relative_path,
                    "serialization_format": SklearnSerializationFormat.JOBLIB,
                },
            },
            {
                "input": {
                    "framework": XGBoostFramework(model_filepath=model_relative_path),
                    "model_file_or_folder": model_filepath,
                },
                "expected": {
                    "model_filepath": model_relative_path,
                    "serialization_format": XGBoostSerializationFormat.JOBLIB,
                },
            },
            {
                "input": {
                    "framework": SklearnFramework(
                        serialization_format=SklearnSerializationFormat.JOBLIB
                    ),
                    "model_file_or_folder": model_relative_path,
                },
                "expected": {
                    "model_filepath": None,
                    "serialization_format": SklearnSerializationFormat.JOBLIB,
                },
            },
            {
                "input": {
                    "framework": XGBoostFramework(
                        serialization_format=XGBoostSerializationFormat.JOBLIB
                    ),
                    "model_file_or_folder": model_relative_path,
                },
                "expected": {
                    "model_filepath": None,
                    "serialization_format": XGBoostSerializationFormat.JOBLIB,
                },
            },
        ]
        self.validate_test_cases(test_cases)

    def test_auto_update_model_framework_details_3(self):
        """
        TestCases: Directory structure:
            - folder
                - model.joblib
        """
        self.create_dummy_model_file(
            os.path.join(self.model_dir, Path("folder/model.joblib"))
        )
        test_cases = [
            {
                "input": {
                    "framework": SklearnFramework(),
                    "model_file_or_folder": self.model_dir,
                },
                "expected": {
                    "model_filepath": "folder/model.joblib",
                    "serialization_format": SklearnSerializationFormat.JOBLIB,
                },
            },
            {
                "input": {
                    "framework": XGBoostFramework(),
                    "model_file_or_folder": self.model_dir,
                },
                "expected": {
                    "model_filepath": "folder/model.joblib",
                    "serialization_format": XGBoostSerializationFormat.JOBLIB,
                },
            },
        ]
        self.validate_test_cases(test_cases)

        framework = XGBoostFramework(model_filepath="folder/model_2.joblib")
        with pytest.raises(FileNotFoundError):
            auto_update_model_framework_details(
                framework=framework, model_file_or_folder=self.model_dir
            )

    def test_auto_update_model_framework_details_4(self):
        """
        TestCases: Directory structure:
            - folder
                - model.joblib
        - Other model file in a different directory
            - other_model.joblib
        """
        self.create_dummy_model_file(
            os.path.join(self.model_dir, Path("folder/model.joblib"))
        )
        with tempfile.TemporaryDirectory() as other_model_dir:
            other_model_filepath = os.path.join(other_model_dir, "other_model.joblib")
            self.create_dummy_model_file(other_model_filepath)

            # Case 1: Model file path specified in a different directory
            framework = XGBoostFramework(model_filepath=other_model_filepath)
            with pytest.raises(ValueError):
                auto_update_model_framework_details(
                    framework=framework, model_file_or_folder=self.model_dir
                )

    def test_sklearn_infer_schema(self):
        """
        Test sklearn_infer_schema function
        """
        # Case: Test infer schema for predict method, Valid
        model_input = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]], dtype=np.int64)
        model = joblib.load(self.sample_model_file)
        model_schema = sklearn_infer_schema(
            model_input=model_input, model=model, infer_method_name="predict"
        )
        assert model_schema.infer_method_name == InferMethodName.PREDICT
        assert len(model_schema.inputs) == 1
        assert len(model_schema.outputs) == 1
        assert model_schema.inputs[0] == {
            "type": "tensor",
            "tensor-spec": {"dtype": "int64", "shape": [-1, 2]},
        }
        assert model_schema.outputs[0] == {
            "type": "tensor",
            "tensor-spec": {"dtype": "int64", "shape": [-1]},
        }

        # Case: Test infer schema for predict_proba method, Invalid
        infer_method_name = "predict_proba"
        with pytest.raises(
            ValueError,
            match=f"Model does not have the method '{infer_method_name}' to infer the schema.",
        ):
            sklearn_infer_schema(
                model_input=model_input,
                model=model,
                infer_method_name=infer_method_name,
            )

    def test_xgboost_infer_schema(self):
        """
        Test xgboost_infer_schema function
        """
        # Case: Test infer schema for predict method, Valid
        model_input = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]], dtype=np.int32)
        model = joblib.load("tests/ml/data/xgboost-model.joblib")
        model_schema = xgboost_infer_schema(
            model_input=model_input, model=model, infer_method_name="predict"
        )
        assert model_schema.infer_method_name == InferMethodName.PREDICT
        assert len(model_schema.inputs) == 1
        assert len(model_schema.outputs) == 1
        assert model_schema.inputs[0] == {
            "type": "tensor",
            "tensor-spec": {"dtype": "int32", "shape": [-1, 2]},
        }
        assert model_schema.outputs[0] == {
            "type": "tensor",
            "tensor-spec": {
                "dtype": "int32",
                "shape": [-1],
            },  # XGBoost returns int32 on windows
        } or model_schema.outputs[0] == {
            "type": "tensor",
            "tensor-spec": {
                "dtype": "int64",
                "shape": [-1],
            },  # XGBoost returns int64 on linux, mac
        }

        # Case: Test infer schema for predict_proba method, model is XGBClassifier so method is present, but not valid
        infer_method_name = "predict_proba"
        with pytest.raises(ValidationError):
            xgboost_infer_schema(
                model_input=model_input,
                model=model,
                infer_method_name=infer_method_name,
            )
