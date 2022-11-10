import airflow
from sqlalchemy import create_engine
from datetime import timedelta,datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import os
import pandas as pd

default_args = {
    'owner':'nahom',
    'retries':5,
    'retry_delay':timedelta(minutes=2)
}

# def load_raw_data(path, table_name):
#     print("writing data..............")
#     engine = create_engine("postgresql://postgres:9XYPHxdgEWmSopgCRl1N@containers-us-west-62.railway.app:7977/railway")
#     df = pd.read_csv(path, sep=",", index_col=False)

#     df.to_sql(table_name, con=engine, if_exists='replace',index_label='id')
#     print("!!!!Done!!!!")


# with DAG(
#     dag_id='load_to_dwh_v2',
#     default_args=default_args,
#     description='This loads cleaned data to the postgres warehouse on railway',
#     start_date=airflow.utils.dates.days_ago(1),
#     schedule_interval='@once'
# )as dag:
#     task1 = PythonOperator(
#         task_id='load_raw_data',
#         python_callable=load_raw_data,
#         op_kwargs={
#             "path": "./data/drone3_clean.csv",
#             "table_name":"traffic_raw"
#         }
#     )
#     task1
def read_data():
    df = pd.read_csv('/opt/airflow/data/drone3_clean.csv')
    