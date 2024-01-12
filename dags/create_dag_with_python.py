from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator


def greet(ti):
    first_name = ti.xcom_pull(task_ids="get_name", key="first_name")
    last_name = ti.xcom_pull(task_ids="get_name", key="last_name")
    age = ti.xcom_pull(task_ids="get_age", key="age")
    print(f"Hello {first_name} {last_name}, you are {age} years old!")


def get_name(ti):
   ti.xcom_push(key="first_name", value="Shash")
   ti.xcom_push(key="last_name", value="Kularatna")


def get_age(ti):
    ti.xcom_push(key="age", value=25)


default_args = {
    "owner": "shash",
    "retry": 5,
    "retry_delay": timedelta(minutes=2),
}

with DAG(
    dag_id="dag_with_python_operator_8",
    default_args=default_args,
    description="DAG using pyhton operator ",
    start_date=datetime(2024, 1, 1, 2),
    schedule_interval="@daily"
) as dag:
    task1 = PythonOperator(
        task_id="greet",
        python_callable=greet,
    )

    task2 = PythonOperator(
        task_id="get_name",
        python_callable=get_name
    )

    task3 = PythonOperator(
        task_id="get_age",
        python_callable=get_age
    )

    [task2, task3] >> task1