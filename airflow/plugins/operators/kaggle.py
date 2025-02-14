import kaggle
import os
import zipfile
from pathlib import Path
from kaggle.api.kaggle_api_extended import KaggleApi

def check_kaggle_credentials():
    try:
        api = KaggleApi()
        api.authenticate()
        print("Kaggle API authenticated successfully")
    except Exception as e:
        raise Exception(f"Failed to authenticate Kaggle API: {e}")
    

def download_dataset(dataset_name):
    try:
        api = KaggleApi()
        api.authenticate()
        print("Downloading dataset...")

        # temp_download_path = Path("/tmp")
        # os.makedirs(temp_download_path, exist_ok=True)
        # api.dataset_download_files(dataset_name, path=temp_download_path, unzip=True)
        # print("Dataset downloaded successfully")
    except Exception as e:
        raise Exception(f"Failed to download dataset {dataset_name}: {e}")