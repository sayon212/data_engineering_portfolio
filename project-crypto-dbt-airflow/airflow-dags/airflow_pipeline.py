from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner' : 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 0
}

with DAG (
    dag_id = 'pl001_ingest_crypto_postgres',
    default_args = default_args,
    schedule_interval = None,
    catchup = False

) as dag:
    
    python_ingestion = BashOperator(
        task_id='python_ingestion',
        bash_command='python /opt/scripts/ingest_crypto_data.py'
    )

    dbt_curated_transformations = BashOperator(
        task_id="dbt_curated_transformation",
        bash_command="""
        export DBT_LOG_PATH=/tmp/dbt && \
        mkdir -p /tmp/dbt && \
        cd /opt/airflow/dbt && \
        dbt run 
        """
    )

    python_ingestion >> dbt_curated_transformations