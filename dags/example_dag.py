from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "shash",
    "retry": 5,
    "retry_delay": timedelta(minutes=2),
}

with DAG(
    dag_id="example_dag",
    default_args=default_args,
    description="This is a simple DAG",
    start_date=datetime(2024, 1, 1, 2),
    schedule_interval="@daily"
) as dag:
    task1 = BashOperator(
        task_id="task1",
        bash_command="echo 'This is task 1'",
    )

    task2 = BashOperator(
        task_id="task2",
        bash_command="echo 'This is task 2'",
    )

    task3 = BashOperator(
        task_id="task3",
        bash_command="echo 'This is task 3'",
    )

    task1 >> [task2, task3]
