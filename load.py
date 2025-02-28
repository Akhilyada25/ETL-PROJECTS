from google.cloud import bigquery

def load_to_bigquery():
    client = bigquery.Client()
    table_id = "your_project_id.dataset.transactions"

    job_config = bigquery.LoadJobConfig(write_disposition="WRITE_APPEND")
    
    with open("/tmp/transformed_data/", "rb") as source_file:
        job = client.load_table_from_file(source_file, table_id, job_config=job_config)
    job.result()
