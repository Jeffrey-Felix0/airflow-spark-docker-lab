from airflow import DAG
from datetime import datetime

with DAG(
    dag_id="spark_test_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
):
    pass
