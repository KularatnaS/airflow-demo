from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    "owner": "shash",
    "retry": 5,
    "retry_delay": timedelta(minutes=2),
    "catchup": False
}


def get_sklearn():
    import sklearn
    print(f'sklearn version: {sklearn.__version__}')

with DAG(
    dag_id="dag_with_custom_python_packages",
    default_args=default_args,
    description="DAG using pyhton operator ",
    start_date=datetime(2024, 1, 1, 2),
    schedule_interval="@daily"
) as dag:
    get_sklearn = PythonOperator(
        task_id="get_sklearn",
        python_callable=get_sklearn,
    )
    get_sklearn