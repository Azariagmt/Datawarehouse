from airflow import DAG
from airflow.operators.mysql_operator import MySqlOperator

default_arg = {'owner': 'airflow', 'start_date': '2020-02-28'}

dag = DAG('simple-mysql-dag',
          default_args=default_arg,
          schedule_interval='@once')

mysql_task = MySqlOperator(dag=dag,
                           mysql_conn_id='local_mysql', 
                           task_id='mysql_task',
                           sql='/user/local/airflow/include/sample_sql.sql ',
                           params={'test_user_id': -99})


mysql_task