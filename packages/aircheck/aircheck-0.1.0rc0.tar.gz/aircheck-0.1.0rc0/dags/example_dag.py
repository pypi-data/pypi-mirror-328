from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator

# Default arguments for the DAG
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 1, 1),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# Define the DAG
with DAG(
    dag_id="example_dag",
    default_args=default_args,
    description="An example DAG for testing",
    schedule_interval="@daily",
    catchup=False,
) as dag:
    start = DummyOperator(task_id="start")

    def print_hello():
        print("Hello from Airflow!")

    task1 = PythonOperator(
        task_id="print_hello",
        python_callable=print_hello,
    )

    end = DummyOperator(task_id="end")

    # Define the task dependencies
    start >> task1 >> end


with DAG(
    dag_id="example_dag1",
    default_args=default_args,
    description="An example DAG for testing",
    schedule_interval="@daily",
    catchup=False,
) as dag1:
    ...
