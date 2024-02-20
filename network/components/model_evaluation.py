import os
import sys
import json
import numpy as np
import mlflow
from typing import Dict
from tensorflow import keras
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

from network.utils import main_utils
from config.config import params
from network.constant import training_pipeline
from network.entity.artifact_entity import (
    DataTransformationArtifact,
    ModelEvaluationArtifact,
    ModelTrainerArtifact
)
from network.entity.config_entity import ModelEvaluationConfig
from network.exception import NetworkException
from network.logger import logging
from network.configuration.mlflow_connection import MLFlowClient


class ModelEvaluator:
    def __init__(self,
                 model_trainer_artifact: ModelTrainerArtifact,
                 model_evaluation_config: ModelEvaluationConfig):
        self.model_trainer_artifact = model_trainer_artifact
        self.model_evaluation_config = model_evaluation_config
        self.model = keras.models.load_model(self.model_trainer_artifact.best_model_path)
        self.mlflow_client = MLFlowClient()

    def evaluate_model(self, x_test, y_test):
        # Start a new MLflow run for evaluation
        mlflow.start_run()
        mlflow.tensorflow.autolog()  # Enable autologging for TensorFlow

        # Make predictions on the test data
        y_pred = self.model.predict(x_test)

        # Calculate various evaluation metrics
        accuracy = accuracy_score(y_test, y_pred.round())
        precision = precision_score(y_test, y_pred.round())
        recall = recall_score(y_test, y_pred.round())
        f1 = f1_score(y_test, y_pred.round())

        # Log evaluation metrics to MLflow
        mlflow.log_metrics({
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1_score": f1
        })

        logging.info(f"Accuracy: {accuracy}, Precision: {precision}, Recall: {recall}, F1-score: {f1}")

        # Log additional metrics or plots if needed

        # End the MLflow run
        mlflow.end_run()

    def initiate_model_evaluation(self) -> ModelEvaluationArtifact:
        try:
            # Load test data using main_utils or your preferred method
            x_test, y_test = ...  # Load test data

            # Perform model evaluation
            self.evaluate_model(x_test, y_test)

            # Create and return ModelEvaluationArtifact with metrics or summaries
            model_evaluation_artifact = ModelEvaluationArtifact(
                metrics={
                    "accuracy": accuracy,
                    "precision": precision,
                    "recall": recall,
                    "f1_score": f1
                }
            )

            return model_evaluation_artifact

        except Exception as e:
            raise NetworkException(e, sys)

