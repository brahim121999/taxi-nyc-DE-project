# %%
import io
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, isnan, when, count
import pyarrow.parquet as pq
from google.cloud import storage

# %%
# start a Spark session
spark = SparkSession.builder \
    .appName("YellowTripData") \
    .getOrCreate()

# %%
# load the Parquet file into a DataFrame
file_path = "data/yellow_tripdata_2022-01.parquet"
yellow_tripdata_df = spark.read.parquet(file_path)

# %%
# display the first few entries of the DataFrame
yellow_tripdata_df.show()

# %%
# print the structure of the DataFrame
yellow_tripdata_df.printSchema()

# %%
# build a list to calculate missing entries per column
missing_values = yellow_tripdata_df.select(
    [
        count(when(col(c).isNull(), c)).alias(c)
        for c in yellow_tripdata_df.columns
    ]
)

# show the count of missing values for each column
missing_values.show()

# %%
PROJECT_ID = "taxi-project-461423"
BUCKET_NAME = f"{PROJECT_ID}-data-bucket"
GCS_FOLDER = "dataset/trips/"

storage_client = storage.Client()

# examine parquet file schema
def inspect_parquet_schema(file_name):
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(f"{GCS_FOLDER}{file_name}")

    file_stream = io.BytesIO()
    blob.download_to_file(file_stream)
    file_stream.seek(0)

    table = pq.read_table(file_stream)
    print(table.schema)


inspect_parquet_schema("yellow_tripdata_2025-03.parquet")