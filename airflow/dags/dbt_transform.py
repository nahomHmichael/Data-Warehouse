import airflow
from airflow.utils.dates import days_ago

from sqlalchemy import create_engine
from datetime import timedelta,datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash_operator import BashOperator
import os
import pandas as pd

default_args = {
    "owner": "nahom",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag_execute = DAG(
    dag_id="dbt_orchestrate",
    default_args=default_args,
    schedule_interval="@daily",
    start_date=days_ago(1),
    dagrun_timeout=timedelta(minutes=60),
    description="executing dag scripts",
)

 
dbt_run = BashOperator(task_id="dbt_run",
        bash_command=f"dbt run --project-dir /opt/airflow/dbt --profiles-dir .. ",dag=dag_execute)
dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=f"dbt test --project-dir /opt/airflow/dbt --profiles-dir ..",dag=dag_execute)
dbt_docs_generate = BashOperator(
        task_id="dbt_doc_gen", 
        bash_command=f"dbt docs generate --project-dir /opt/airflow/dbt --profiles-dir .. ",dag=dag_execute)

dbt_run >> dbt_test >> dbt_docs_generate