from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    "owner": "shash",
    "retry": 5,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="dag_with_cron_2",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval="0 3 * * Tue,Fri",
    catchup=True
) as dag:
    task1 = BashOperator(
        task_id="task1",
        bash_command="echo dag with cron",
    )

    task1