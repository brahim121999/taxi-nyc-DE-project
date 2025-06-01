import logging
from google.cloud import bigquery, storage
from datetime import datetime
import io
from datetime import UTC

# project variables
PROJECT_ID = "taxi-project-461423"
BUCKET_NAME = f"{PROJECT_ID}-data-bucket"
GCS_FOLDER = "dataset/trips/"
GCS_LOG_FOLDER = "from-git/logs/"
TABLE_ID = f"{PROJECT_ID}.taxitrips.trips"
TEMP_TABLE_ID = f"{TABLE_ID}_temp" # temporary table to load data without type constraints

# initialize bigquery and gcs client
bq_client = bigquery.Client(project=PROJECT_ID, location="EU")
storage_client = storage.Client()

# set up logging
log_stream = io.StringIO()
logging.basicConfig(stream=log_stream, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def upload_log_to_gcs():
    log_filename = f"{GCS_LOG_FOLDER}load_log_{datetime.now(UTC).strftime('%Y%m%d_%H%M%S')}.log"
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(log_filename)
    blob.upload_from_string(log_stream.getvalue())
    logging.info(f"Log file uploaded to {log_filename}")

def get_existing_files():
    query = f"""
        SELECT DISTINCT source_file 
        FROM `{TABLE_ID}`
        WHERE source_file IS NOT NULL
    """
    query_job = bq_client.query(query, location="EU")
    return {row.source_file for row in query_job.result()}

def get_gcs_files():
    bucket = storage_client.bucket(BUCKET_NAME)
    blobs = bucket.list_blobs(prefix=GCS_FOLDER)
    return {blob.name.split('/')[-1] for blob in blobs if blob.name.endswith(".parquet")}

def load_new_files():
    try:
        new_files = get_gcs_files() - get_existing_files()

        if not new_files:
            logging.info("No new files to load")
            return

        for file in new_files:
            url = f"gs://{BUCKET_NAME}/{GCS_FOLDER}{file}"
            logging.info(f"Loading file: {url}")

            # load file into temporary table without forcing
            temp_job_config = bigquery.LoadJobConfig(
                source_format = bigquery.SourceFormat.PARQUET,
                write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
                autodetect=True
            )

            load_job = bq_client.load_table_from_url(url, TEMP_TABLE_ID, job_config=temp_job_config)
            load_job.result()
            logging.info(f"Loaded file into: {TEMP_TABLE_ID}")

            # 2) transformation and insertion with passenger_count conversion
            query = f"""
            INSERT INTO `{TABLE_ID}`
            SELECT 
                VendorID, 
                tpep_pickup_datetime, 
                tpep_dropoff_datetime, 
                CAST(passenger_count AS FLOAT64) AS passenger_count,
                trip_distance, 
                RatecodeID, 
                store_and_fwd_flag, 
                PULocationID, 
                DOLocationID, 
                payment_type, 
                fare_amount, 
                extra, 
                mta_tax, 
                tip_amount, 
                tolls_amount, 
                improvement_surcharge, 
                total_amount, 
                congestion_surcharge, 
                airport_fee,
                "{file}" AS source_file
            FROM `{TEMP_TABLE_ID}`
            """

            query_job = bq_client.query(query)
            query_job.result()
            logging.info(f" Data from{TEMP_TABLE_ID} inserted into {TABLE_ID}")

            # delete temp table
            bq_client.delete_table(TEMP_TABLE_ID, not_found_ok=True)
            logging.info(f" Deleted temp table {TEMP_TABLE_ID}")

        destination_table = bq_client.get_table(TABLE_ID)
        logging.info(f"Loaded {destination_table.num_rows} rows into table {TABLE_ID}")

    except Exception as e:
        logging.error(f"Error in laoding : {str(e)}")
    finally:
        upload_log_to_gcs()



load_new_files()

