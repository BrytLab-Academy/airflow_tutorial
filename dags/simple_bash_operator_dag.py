from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'phil',
    'retries': 5,
    'retry_delay': timedelta(2),
}


with DAG(
    dag_id='simple_bash_operator',
    default_args=default_args,
    description='A simple bash operator',
    start_date=datetime(2023,11,23,0),
    schedule_interval='@daily'
)as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command='echo This is my first task'
    )
    task2 = BashOperator(
        task_id='second_task',
        bash_command='echo This is the second task'
    )

task1 >> task2

