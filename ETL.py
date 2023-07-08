import os
from google.cloud import storage
from google.cloud import bigquery

def extract_transform_load(bucket_name, object_name, dataset_id, table_id):
    # Initialize Google Cloud Storage client
    storage_client = storage.Client()

    # Get the source file from the bucket
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(object_name)

    # Download the file to a local temporary location
    temp_file_path = "temp_file.xlsx"
    blob.download_to_filename(temp_file_path)

    # Initialize BigQuery client
    bigquery_client = bigquery.Client()

    # Create a BigQuery dataset reference
    dataset_ref = bigquery_client.dataset(dataset_id)

    # Create a BigQuery table reference
    table_ref = dataset_ref.table(table_id)

    # Load the data into BigQuery table
    job_config = bigquery.LoadJobConfig(
        schema=[
            # Define the schema of the table
            bigquery.SchemaField("full_name_donor", "STRING"),
            bigquery.SchemaField("email_address", "STRING"),
            bigquery.SchemaField("hear_about_us", "STRING"),
            bigquery.SchemaField("drop_off_location", "STRING"),
            bigquery.SchemaField("bike_make_model", "STRING"),
            bigquery.SchemaField("bike_color", "STRING"),
            bigquery.SchemaField("bike_wheel_size", "STRING"),

            # Add more fields as per your dataset schema
        ],
        skip_leading_rows=1,  # If the file has a header row, set this to skip it
        source_format=bigquery.SourceFormat.CSV,
    )

    with open(temp_file_path, "rb") as source_file:
        job = bigquery_client.load_table_from_file(
            source_file, table_ref, job_config=job_config
        )

    job.result()  # Wait for the job to complete

    print(f"Data loaded into BigQuery table {table_id} successfully.")

    # Delete the temporary file
    os.remove(temp_file_path)

# Example usage
bucket_name = "bworks-donor-bucket"
object_name = "Donor.csv"
dataset_id = "donor_data"
table_id = "bicycles_data"

extract_transform_load(bucket_name, object_name, dataset_id, table_id)
