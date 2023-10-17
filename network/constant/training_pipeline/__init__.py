#here we will be mentoning all the constants required.

import os
from datetime import datetime

import numpy as np

TIMESTAMP = datetime = datetime.now().strftime("%m_%d_%Y")
PIPELINE_NAME: str = "network-intrusion"
ARTIFACTS_DIR: str = "artifacts"
#names of dirs. this dirs or pipeline code in congig_entity.py file.


"""
Constants related to Data Ingestion stage
"""
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_BUCKET_NAME: str = "networkdata1"
DATA_INGESTION_BUCKET_FOLDER_NAME: str = "data/traindata"
DATA_INGESTION_FEATURE_STORE_FOLDER_DIR: str = "feature_store" #this is local dir where feature is stored and created.
