from airflow import DAG
from airflow.operators.mysql_operator import MySqlOperator

default_arg = {'owner': 'airflow', 'start_date': '2020-02-28'}

dag = DAG('load-data',
          default_args=default_arg,
          schedule_interval='@once',
          template_searchpath=['/usr/local/airflow/include/'])

create_I80_stations = MySqlOperator(dag=dag,
                           mysql_conn_id='mysql-connect', 
                           task_id='create_I80_stations',
                            sql='create_I80_stations.sql')


load_I80_stations = MySqlOperator(dag=dag,
                           mysql_conn_id='mysql-connect', 
                           task_id='load_stations',
                            sql='load_I80_stations.sql')



create_I80_stations >> load_I80_stations 