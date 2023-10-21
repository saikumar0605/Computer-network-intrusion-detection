import sys
import os

from network.components.data_ingestion import DataIngestion
from network.components.data_validation import DataValidation


from network.entity.artifact_entity import (
    DataIngestionArtifact,
    DataValidationArtifact,
)

from network.entity.config_entity import (
    TrainingPipelineConfig,
    DataIngestionConfig,
    DataValidationConfig,
)

from network.exception import NetworkException

class TrainingPipeline:
    def __init__(self ) -> None:
        self.training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig()
    
    #starting data ingestion. defining it... -> this symbol is used to define the output. will be that particular artifact or file.
    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            self.data_ingestion_config: DataIngestionConfig = DataIngestionConfig(
                training_pipeline_config= self.training_pipeline_config
            )

            data_ingestion: DataIngestion = DataIngestion(
                data_ingestion_config= self.data_ingestion_config
            )
            data_ingestion_artifact: DataIngestionArtifact = DataIngestionArtifact(
                data_ingestion.initiate_data_ingestion()
            )
            #data_ingestion.initiate_data_ingestion() this def fun is defined in training pipeline so we initiate to start.
            return data_ingestion_artifact
        
        except Exception as e:
            raise NetworkException(e, sys)
        
    def start_data_validation(self, 
                              data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
        try:
            self.data_validation_config: DataValidationConfig = DataValidationConfig(
                training_pipeline_config= self.training_pipeline_config
            )

            data_validation: DataValidation = DataValidation(
                data_ingestion_artifact = data_ingestion_artifact,
                data_validation_config= self.data_validation_config
            )

            data_validation_artifact: DataValidationArtifact = DataValidationArtifact(
                data_validation.initiate_data_validation()
            )

            return data_validation_artifact
        
        except Exception as e:
            raise NetworkException(e, sys)
    


    def run_pipeline(self):
        try:
            data_ingestion_artifact: DataIngestionArtifact =  self.start_data_ingestion()
            data_validation_artifact: DataValidationArtifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            return data_validation_artifact
        
        except Exception as e:
            raise NetworkException(e, sys)