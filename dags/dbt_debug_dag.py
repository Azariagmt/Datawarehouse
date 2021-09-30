from airflow import DAG 
from airflow.operators.bash_operator import BashOperator 
from datetime import timedelta 

default_args = {
    'owner': 'airflow',
    'start_date': '2020-02-28'
}

with DAG(
    'dbt-debug',
    default_args=default_args,
    description='DAG to debug dbt project',
    schedule_interval=timedelta(days=1),
    tags=['dbt', 'debug'],
) as dag:
    dbt_debug = BashOperator(
        task_id="dbt_debug",
        bash_command='dbt debug',
        # env: Optional[Dict[str, str]] = None,
        # output_encoding: str = 'utf-8',
        # skip_exit_code: int = 99,
    )