# smolmodels/models.py

"""
This module defines the `Model` class, which represents a machine learning model.

A `Model` is characterized by a natural language description of its intent, structured input and output schemas,
and optional constraints that the model must satisfy. This class provides methods for building the model, making
predictions, and inspecting its state, metadata, and metrics.

Key Features:
- Intent: A natural language description of the model's purpose.
- Input/Output Schema: Defines the structure and types of inputs and outputs.
- Constraints: Rules that must hold true for input/output pairs.
- Mutable State: Tracks the model's lifecycle, training metrics, and metadata.
- Build Process: Integrates solution generation with directives and callbacks.

Example:
>>>    model = Model(
>>>        intent="Given a dataset of house features, predict the house price.",
>>>        output_schema={"price": float},
>>>        input_schema={
>>>            "bedrooms": int,
>>>            "bathrooms": int,
>>>            "square_footage": float
>>>        }
>>>    )
>>>
>>>    model.build(dataset=pd.read_csv("houses.csv"), provider="openai:gpt-4o-mini", max_iterations=10)
>>>
>>>    prediction = model.predict({"bedrooms": 3, "bathrooms": 2, "square_footage": 1500.0})
>>>    print(prediction)
"""

import logging
import types
import uuid
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Dict, Union, List, Literal, Any

import numpy as np
import pandas as pd
import os

from smolmodels.callbacks import Callback
from smolmodels.config import config
from smolmodels.constraints import Constraint
from smolmodels.directives import Directive
from smolmodels.internal.common.datasets.adapter import DatasetAdapter
from smolmodels.internal.common.provider import Provider
from smolmodels.internal.datasets.generator import generate_data, DataGenerationRequest
from smolmodels.internal.models.generation.schema import generate_schema_from_dataset, generate_schema_from_intent
from smolmodels.internal.models.generators import ModelGenerator


class ModelState(Enum):
    DRAFT = "draft"
    BUILDING = "building"
    READY = "ready"
    ERROR = "error"


logger = logging.getLogger(__name__)


@dataclass
class ModelReview:
    summary: str
    suggested_directives: List[Directive]
    # todo: this can be fleshed out further


@dataclass
class GenerationConfig:  # todo: move to internal/datasets
    """Configuration for data generation/augmentation"""

    n_samples: int
    augment_existing: bool = False
    quality_threshold: float = 0.8

    def __post_init__(self):
        if self.n_samples <= 0:
            raise ValueError("Number of samples must be positive")
        if not 0 <= self.quality_threshold <= 1:
            raise ValueError("Quality threshold must be between 0 and 1")

    @classmethod
    def from_input(cls, value: Union[int, Dict[str, Any]]) -> "GenerationConfig":
        """Create config from either number or dictionary input"""
        if isinstance(value, int):
            return cls(n_samples=value)
        elif isinstance(value, dict):
            return cls(
                n_samples=value["n_samples"],
                augment_existing=value.get("augment_existing", False),
                quality_threshold=value.get("quality_threshold", 0.8),
            )
        raise ValueError(f"Invalid generate_samples value: {value}")


class Model:
    """
    Represents a model that transforms inputs to outputs according to a specified intent.

    A `Model` is defined by a human-readable description of its expected intent, as well as structured
    definitions of its input schema, output schema, and any constraints that must be satisfied by the model.

    Attributes:
        intent (str): A human-readable, natural language description of the model's expected intent.
        output_schema (dict): A mapping of output key names to their types.
        input_schema (dict): A mapping of input key names to their types.
        constraints (List[Constraint]): A list of Constraint objects that represent rules which must be
            satisfied by every input/output pair for the model.

    Example:
        model = Model(
            intent="Given a dataset of house features, predict the house price.",
            output_schema={"price": float},
            input_schema={
                "bedrooms": int,
                "bathrooms": int,
                "square_footage": float,
            }
        )
    """

    def __init__(
        self, intent: str, output_schema: dict = None, input_schema: dict = None, constraints: List[Constraint] = None
    ):
        """
        Initialise a model with a natural language description of its intent, as well as
        structured definitions of its input schema, output schema, and any constraints.

        :param [str] intent: A human-readable, natural language description of the model's expected intent.
        :param [dict] output_schema: A mapping of output key names to their types.
        :param [dict] input_schema: A mapping of input key names to their types.
        :param List[Constraint] constraints: A list of Constraint objects that represent rules which must be
            satisfied by every input/output pair for the model.
        """
        # todo: analyse natural language inputs and raise errors where applicable

        # The model's identity is defined by these fields
        self.intent = intent
        self.output_schema = output_schema
        self.input_schema = input_schema
        self.constraints = constraints or []
        self.training_data: pd.DataFrame | None = None

        # The model's mutable state is defined by these fields
        self.state = ModelState.DRAFT
        self.predictor: types.ModuleType | None = None
        self.trainer_source: str | None = None
        self.predictor_source: str | None = None
        self.artifacts: List[Path] = []
        self.metrics: Dict[str, str] = dict()
        self.metadata: Dict[str, str] = dict()  # todo: initialise metadata, etc

        # Unique identifier for the model, used in directory paths etc
        self.identifier: str = f"model-{abs(hash(self.intent))}-{str(uuid.uuid4())}"
        # Directory for any required model files
        base_dir = os.environ.get("MODEL_PATH", config.file_storage.model_cache_dir)
        self.files_path: Path = Path(base_dir) / self.identifier

    def build(
        self,
        dataset: pd.DataFrame | np.ndarray = None,
        directives: List[Directive] = None,
        generate_samples: Union[int, Dict[str, Any]] = None,
        callbacks: List[Callback] = None,
        isolation: Literal["local", "subprocess", "docker"] = "local",
        provider: str = "openai/gpt-4o-mini",
        timeout: int = None,
        max_iterations: int = None,
    ) -> None:
        """
        Build the model using the provided dataset, directives, and optional data generation configuration.

        :param dataset: the dataset to use for training the model
        :param directives: instructions related to the model building process - not the model itself
        :param generate_samples: synthetic data generation configuration
        :param callbacks: functions that are called during the model building process
        :param isolation: level of isolation under which model build should be executed
        :param provider: the provider to use for model building
        :param timeout: maximum time in seconds to spend building the model
        :param max_iterations: maximum number of iterations to spend building the model
        :return:
        """
        try:
            provider = Provider(model=provider)
            self.state = ModelState.BUILDING

            # Step 1: Resolve Schema
            if dataset is not None:
                self.training_data = DatasetAdapter.convert(dataset)

                if self.input_schema is None and self.output_schema is None:
                    self.input_schema, self.output_schema = generate_schema_from_dataset(
                        provider=provider, intent=self.intent, dataset=self.training_data
                    )
                elif self.output_schema is None:
                    _, self.output_schema = generate_schema_from_dataset(
                        provider=provider, intent=self.intent, dataset=self.training_data
                    )
                elif self.input_schema is None:
                    self.input_schema, _ = generate_schema_from_dataset(
                        provider=provider, intent=self.intent, dataset=self.training_data
                    )
            else:
                if self.input_schema is None or self.output_schema is None:
                    self.input_schema, self.output_schema = generate_schema_from_intent(
                        provider=provider, intent=self.intent
                    )

            # Step 2: Handle Data (now we have schemas)
            if dataset is not None:
                # Ensure training data is loaded
                if self.training_data is None:
                    self.training_data = DatasetAdapter.convert(dataset)

                # Handle optional augmentation
                if generate_samples is not None:
                    datagen_config = GenerationConfig.from_input(generate_samples)
                    request = DataGenerationRequest(
                        intent=self.intent,
                        input_schema=self.input_schema,
                        output_schema=self.output_schema,
                        n_samples=datagen_config.n_samples,
                        augment_existing=True,
                        quality_threshold=datagen_config.quality_threshold,
                        existing_data=self.training_data,
                    )
                    synthetic_data = generate_data(provider, request)
                    self.training_data = pd.concat([self.training_data, synthetic_data], ignore_index=True)

            elif generate_samples is not None:
                # Generate new data
                datagen_config = GenerationConfig.from_input(generate_samples)
                request = DataGenerationRequest(
                    intent=self.intent,
                    input_schema=self.input_schema,
                    output_schema=self.output_schema,
                    n_samples=datagen_config.n_samples,
                    augment_existing=False,
                    quality_threshold=datagen_config.quality_threshold,
                    existing_data=None,
                )
                self.training_data = generate_data(provider, request)

            else:
                raise ValueError("No data available. Provide dataset or generate_samples.")

            # todo: keep the model generator across multiple build() calls
            # Step 3: Generate Model
            model_generator = ModelGenerator(
                self.intent, self.input_schema, self.output_schema, provider, self.files_path, self.constraints
            )
            generated = model_generator.generate(self.training_data, timeout, max_iterations, directives)

            self.trainer_source = generated.training_source_code
            self.predictor_source = generated.inference_source_code
            self.predictor = generated.inference_module
            self.artifacts = generated.model_artifacts
            self.metrics = generated.performance

            self.state = ModelState.READY
        except Exception as e:
            self.state = ModelState.ERROR
            logger.error(f"Error during model building: {str(e)}")
            raise e

    def predict(self, x: dict) -> dict:
        """
        Call the model with input x and return the output.
        :param x: input to the model
        :return: output of the model
        """
        if self.state != ModelState.READY:
            raise RuntimeError("The model is not ready for predictions.")
        try:
            return self.predictor.predict(x)
        except Exception as e:
            raise RuntimeError(f"Error during prediction: {str(e)}") from e

    def get_state(self) -> ModelState:
        """
        Return the current state of the model.
        :return: the current state of the model
        """
        return self.state

    def get_metadata(self) -> dict:
        """
        Return metadata about the model.
        :return: metadata about the model
        """
        return self.metadata

    def get_metrics(self) -> dict:
        """
        Return metrics about the model.
        :return: metrics about the model
        """
        return self.metrics

    def describe(self) -> dict:
        """
        Return a human-readable description of the model.
        :return: a human-readable description of the model
        """
        return {
            "intent": self.intent,
            "output_schema": self.output_schema,
            "input_schema": self.input_schema,
            "constraints": [str(constraint) for constraint in self.constraints],
            "state": self.state,
            "metadata": self.metadata,
            "metrics": self.metrics,
        }

    def review(self) -> ModelReview:
        """
        Return a review of the model, which is a structured object consisting of a natural language
        summary, suggested directives to apply, and more.
        :return: a review of the model
        """
        raise NotImplementedError("Review functionality is not yet implemented.")
