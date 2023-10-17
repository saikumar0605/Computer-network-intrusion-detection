import sys
import os

from network.components.data_ingestion import DataIngestion

from network.entity.artifact_entity import (
    DataIngestionArtifact
)

from network.entity.config_entity import (
    TrainingPipelineConfig,
    DataIngestionConfig
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

    def run_pipeline(self):
        try:
            data_ingestion_artifact: DataIngestionArtifact =  self.start_data_ingestion()
            return data_ingestion_artifact
        
        except Exception as e:
            raise NetworkException(e, sys)