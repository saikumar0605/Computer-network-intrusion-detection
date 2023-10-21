from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    feature_store_folder_path: str

@dataclass
class DataValidationArtifact:
    valid_data_dir: str
    invalid_data_dir: str
    training_file_path: str
    testing_file_path: str    