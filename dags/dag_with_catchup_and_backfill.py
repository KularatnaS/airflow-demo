from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime, timedelta

default_args = {
    "owner": "shash",
    "retry": 5,
    "retry_delay": timedelta(minutes=2),
}

with DAG(
    dag_id="dag_with_catchup_and_backfill",
    default_args=default_args,
    start_date=datetime(2024, 1, 1, 2),
    schedule_interval="@daily",
    catchup=False
) as dag:
    task1 = BashOperator(
        task_id="task1",
        bash_command="echo 'Hello World from Task 1!'"
    )