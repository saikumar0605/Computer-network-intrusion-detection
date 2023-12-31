import os
import sys


from network.exception import NetworkException


class S3Sync:
    def sync_folder_to_s3(self, folder: str, bucket_name: str, bucket_folder_name: str):
        try: 
            command: str = (
                f"aws s3 sync {folder} s3://networkdata1/{bucket_folder_name}/ "
            )
            os.system(command)

        except Exception as e:
            raise NetworkException(e, sys)
        
    def sync_folder_from_s3(
            self, folder: str,bucket_name: str, bucket_folder_name: str
    ) -> None:
        try:
            command: str = (
                f"aws s3 sync s3://networkdata1/{bucket_folder_name}/ {folder}"
            )
            os.system(command)
        except Exception as e:
            raise NetworkException(e, sys)