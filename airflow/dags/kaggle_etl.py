from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from operators.kaggle import check_kaggle_credentials, download_dataset


default_args = {
    'owner': 'Hieu Bui',
    'depends_on_past': False,
    'start_date': datetime(2024, 2, 14),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


with DAG(
    "etl-kaggle-datalake",
    default_args=default_args,
    description="A simple ETL pipeline to download dataset from Kaggle",
    schedule_interval="@quarterly",
    catchup=False,
    max_active_runs=1,
    is_paused_upon_creation=False,
) as dag:
    
    check_kaggle_credentials_task = PythonOperator(
        task_id="check_kaggle_credentials",
        python_callable=check_kaggle_credentials,
        dag=dag,
    )

    download_dataset_task = PythonOperator(
        task_id="download_dataset",
        python_callable=download_dataset,
        op_kwargs={
            "dataset_name": "svanoo/myanimelist-dataset",
            "output_path": "/tmp",
        },
        dag=dag,
    )

    check_kaggle_credentials_task >> download_dataset_task