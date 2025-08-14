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


with DAG('agriculture_climate',
         default_args=default_args,
         schedule_interval='0 0 * * *',
         catchup=False,
         ) as dag:

    extract_data = BashOperator(task_id='extract_data', bash_command='sudo -u airflow python /opt/airflow/scripts/extract.py')
    transform_data = BashOperator(task_id='transform_transform', bash_command='sudo -u airflow python /opt/airflow/scripts/transform.py')
    load_data = BashOperator(task_id='load_data', bash_command='sudo -u airflow python /opt/airflow/scripts/load.py')
    

extract_data >> transform_data >> load_data