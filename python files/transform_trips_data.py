import logging
from google.cloud import bigquery, storage
from datetime import datetime
import io
from datetime import UTC

# project variables
PROJECT_ID = "taxi-project-461423"
RAW_TABLE = f"{PROJECT_ID}.taxitrips.trips"
TRANSFORMED_TABLE = f"{PROJECT_ID}.transformed_data.cleaned_and_filtered"
GCS_LOG_FOLDER = "from-git/logs/"
BUCKET_NAME = f"{PROJECT_ID}-data-bucket"

# initialize bigquery and gcs client
client = bigquery.Client(project=PROJECT_ID, location="EU")
storage_client = storage.Client()

# set up logging
log_stream = io.StringIO()
logging.basicConfig(stream=log_stream, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def upload_log_to_gcs():
    # send the log file to GCS with a timestamp
    log_filename = f"{GCS_LOG_FOLDER}transform_log_{datetime.now(UTC).strftime('%Y%m%d_%H%M%S')}.log"
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(log_filename)
    blob.upload_from_string(log_stream.getvalue())
    logging.info(f"log file sent to {log_filename}")

# the SQL query to clean and filter data
QUERY = f"""
CREATE OR REPLACE TABLE `{TRANSFORMED_TABLE}` AS
SELECT *
FROM `{RAW_TABLE}`
WHERE passenger_count > 0
  AND trip_distance > 0
  AND payment_type != 6
  AND total_amount > 0
ORDER BY source_file;
"""

def transform_data():
    try:
        logging.info("starting data transform process...")

        query_job = client.query(QUERY)
        query_job.result()

        logging.info(f"table {TRANSFORMED_TABLE} created and filled successfully!")
    except Exception as e:
        logging.error(f"could not create/fill the table: {e}")
    finally:
        upload_log_to_gcs()

transform_data()
