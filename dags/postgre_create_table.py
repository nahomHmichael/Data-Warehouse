from airflow import DAG
from sqlalchemy import create_engine
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
import os
import pandas as pd

args = {'owner':'airflow',
        'retries':5,
        'retry_delay':timedelta(minutes=1)}

def load_data(path, table_name):
    print("writing.............")
    engine = create_engine("postgresql+psycopg2://airflow:airflow@postgres/airflow")
    df = pd.read_csv(path,index_col=False, low_memory=False)
    df1 = df
    df = df1.iloc[:, :10]
    
    df.to_sql(table_name, con=engine, if_exists='replace',index_label='id')
    print("...data saved!")

with DAG(
    dag_id="postgres_operator_dag",
    default_args=args,
    start_date=datetime(2022,9,22,2,15),
    description='An Airflow DAG to create tables',
    schedule_interval="@once",
) as dag:
    create_pet_table = PythonOperator(
    task_id="create_table",
    python_callable=load_data,
    #postgres_conn_id="postgres_default",
    #sql="sql/traffic_schema.sql",
    op_kwargs={
        'path':'./data/drone3_clean.csv','table_name':'traffic_table'
        
    }
)
    create_pet_table
