import airflow
import os,sys
import pandas as pd

from sqlalchemy import create_engine
from datetime import timedelta,datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

sys.path.append(os.path.abspath(".."))


default_args = {
    'owner':'nahom',
    'retries':5,
    'retry_delay':timedelta(minutes=2)
}

def load_clean_data(path, table_name):
    """task to load clean data to postgres database

    Args:
        path (str): path to clean data 
        table_name (str): database table name
    """
    print("writing data..............")
    engine = create_engine("postgresql+psycopg2://airflow:airflow@postgres/airflow", echo=True)
    df = pd.read_csv(path, sep=",", index_col=False)

    df.to_sql(table_name, con=engine, if_exists='replace',index_label='id')
    print("!!!!Done!!!!")
    
def clean_df(path):
    """function to clean raw data 

    Args:
        path (str): path of the data to be cleaned
    """
    
    df = pd.read_csv(path,sep='[;:]',index_col=False)
    print('data loaded successfully!!!')
    df.columns = df.columns.str.replace(' ','')
    try:
        df.to_csv('./data/cleanned_data.csv',index=False)
    except Exception as e:
        print(f'error: {e}')
    




with DAG(
    dag_id='load_to_dwh_v2',
    default_args=default_args,
    description='This loads cleaned data to the postgres warehouse on railway',
    start_date=airflow.utils.dates.days_ago(1),
    schedule_interval='@once'
)as dag:
    task1 = PythonOperator(
        task_id='load_clean_data',
        python_callable=load_clean_data,
        op_kwargs={
            "path": "./data/cleanned_data.csv",
            "table_name":"traffic_raw"
        }
    )
    task_2 = PythonOperator(
        task_id='extract_and_clean_data',
        python_callable=clean_df,
        op_kwargs={
            "path":"./data/drone3.csv"}
    )
    task_2>>task1
    
    
# def read_data():
#     df = pd.read_csv('/opt/airflow/data/drone3_clean.csv')
    
    