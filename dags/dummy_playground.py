"""Practice airflow in astronmer."""
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime


default_args = {
    'owner': 'jagadish',
    'start_date': datetime(2019, 12, 10)}

dag = DAG(
    'dummy_playground',
    default_args=default_args,
    schedule_interval='@daily')

dummy_task = DummyOperator(
    task_id='dummy_task',
    dag=dag)
