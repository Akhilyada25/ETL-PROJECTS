from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from scripts.extract import stream_kafka_data
from scripts.transform import process_stream_data
from scripts.load import load_to_bigquery

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 2, 28),
    'retries': 1
}

dag = DAG('real_time_etl', default_args=default_args, schedule_interval='@daily')

extract_task = PythonOperator(task_id='extract', python_callable=stream_kafka_data, dag=dag)
transform_task = PythonOperator(task_id='transform', python_callable=process_stream_data, dag=dag)
load_task = PythonOperator(task_id='load', python_callable=load_to_bigquery, dag=dag)

extract_task >> transform_task >> load_task
