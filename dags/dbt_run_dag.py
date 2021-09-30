from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import timedelta

default_args = {'owner': 'airflow', 'start_date': '2020-02-28'}


with DAG(
    'dbt-run',
    default_args=default_args,
    description='A DAG to run dbt run command',
    schedule_interval=timedelta(days=1),
    tags=['dbt', 'run'],
) as dag:
    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command='dbt run',
        # env: Optional[Dict[str, str]] = None,
        # output_encoding: str = 'utf-8',
        # skip_exit_code: int = 99,
    )