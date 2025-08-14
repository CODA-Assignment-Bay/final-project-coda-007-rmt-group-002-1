import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator


default_args = {
    'owner': 'yustika',
    'start_date': dt.datetime(2025, 8, 10),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=600),
}


with DAG('dag_datamart',
         default_args=default_args,
         schedule_interval='0 0 * * *',
         catchup=False,
         ) as dag:

    datamart = BashOperator(task_id='datamart', bash_command='sudo -u airflow python /opt/airflow/scripts/datamart.py')
    

datamart