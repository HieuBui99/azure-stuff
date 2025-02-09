import os
from pathlib import Path

import polars as pl
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

load_dotenv()

uploads = ["./data/anime.csv", "./data/user.csv"]


def ingest_azure():
    connection_string = os.environ.get("AZURE_BLOB_CONNECTION_STRING")
    blob_client = BlobServiceClient.from_connection_string(connection_string)
    container = blob_client.get_container_client("myanimelist")

    for upload in uploads:
        fn = Path(upload).name

        with open(upload, "rb") as data:
            container.upload_blob(name=f"raw-data/{fn}", data=data, overwrite=True)


ingest_azure()
