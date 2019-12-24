"""Practice airflow in astronmer."""
from airflow import DAG
from airflow.contrib.sensors import 
from datetime import datetime


default_args = {
    'owner': 'jagadish',
    'start_date': datetime(2019, 12, 10)}

dag = DAG(
    'sensor_playground',
    default_args=default_args,
    schedule_interval='@daily')


def hello_world():
    """Hello world."""
    print("hello world")


task1 = PythonOperator(
    task_id='task1',
    python_callable=hello_world,
    dag=dag)
