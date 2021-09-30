from airflow import DAG 
from airflow.operators import BashOperator, PythonOperator 
from datetime import timedelta


default_args = {'owner': 'airflow', 'start_date': '2020-02-28'}

with DAG(
    'redashexport',
    default_args=default_args,
    description='A simple DAG to export redash queries',
    schedule_interval=timedelta(days=1),
    tags=['redash', 'export', 'superset'],
    template_searchpath=['/usr/local/airflow/redash']
) as dag:
    export_redash = PythonOperator(
        task_id="export_redash",
        python_callable='query_export.py',
        # op_kwargs: Optional[Dict] = None,
        # op_args: Optional[List] = None,
        # templates_dict: Optional[Dict] = None
        # templates_exts: Optional[List] = None
    )