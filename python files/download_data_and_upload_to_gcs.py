import requests
import time
from datetime import datetime
from google.cloud import storage
import logging
import io
from io import BytesIO
from datetime import UTC

PROJECT_ID = "taxi-project-461423"
BUCKET_NAME = f"{PROJECT_ID}-data-bucket"
GCS_FOLDER = "dataset/trips/"
GCS_LOG_FOLDER = "from-git/logs/"

# start gcs client
storage_client = storage.Client()

# set up logging
log_stream = io.StringIO()
logging.basicConfig(stream=log_stream, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


# check if file already uploaded
def file_already_uploaded(bucket_name, gcs_path):
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(gcs_path)
    return blob.exists()


# upload file to gcs
def upload_file_to_gcs():
    log_filename = f"{GCS_LOG_FOLDER}extract_log_{datetime.now(UTC).strftime('%Y%m%d_%H%M%S')}.log"
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(log_filename)
    blob.upload_from_string(log_stream.getvalue())
    logging.info(f"Log file uploaded to {log_filename}")


# download data
def download_data():
    current_year = datetime.now().year

    try:
        for year in range(2022, current_year + 1):
            for month in range(1, 13):
                file_name = f"yellow_tripdata_{year}-{month:02d}.parquet"
                gcs_path = f"{GCS_FOLDER}{file_name}"
                download_url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/{file_name}"

                if file_already_uploaded(BUCKET_NAME, gcs_path):
                    logging.info(f"File {file_name} already uploaded to GCS.")
                    continue

                try:
                    logging.info(f"Downloading {file_name}...")
                    response = requests.get(download_url, stream=True)

                    if response.status_code == 200:
                        bucket = storage_client.bucket(BUCKET_NAME)
                        blob = bucket.blob(gcs_path)
                        blob.upload_from_file(BytesIO(response.content))
                        logging.info(f"File {file_name} uploaded to GCS at {gcs_path}")

                    elif response.status_code == 404:
                        logging.warning(f"File {file_name} not found on the server.")

                    else:
                        logging.error(f"Failed to download {file_name}. Status code: {response.status_code}")

                except Exception as e:
                    logging.error(f"Error downloading {file_name}: {str(e)}")

                time.sleep(0.5)

        logging.info("Data download and upload completed.")

    except Exception as e:
        logging.error(f"Error during data download and upload: {str(e)}")

    finally:
        upload_file_to_gcs()


download_data()