"""Practice airflow in astronmer."""
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime


default_args = {
    'owner': 'jagadish',
    'start_date': datetime(2019, 12, 10)}

dag = DAG(
    'bash_playground',
    default_args=default_args,
    schedule_interval='@daily')

task1 = BashOperator(
    task_id='task1',
    bash_command='echo hello_world',
    dag=dag)
