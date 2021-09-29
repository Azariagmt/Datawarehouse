from airflow import DAG
from airflow.operators.mysql_operator import MySqlOperator

default_arg = {'owner': 'airflow', 'start_date': '2020-02-28'}

dag = DAG('load-data',
          default_args=default_arg,
          schedule_interval='@once',
          template_searchpath=['/usr/local/airflow/include/'])

create_table = MySqlOperator(dag=dag,
                           mysql_conn_id='mysql-connect', 
                           task_id='create_table',
                            sql='create_awesome_table.sql')



load_I80_stations = MySqlOperator(dag=dag,
                           mysql_conn_id='mysql-connect', 
                           task_id='load_stations',
                            sql='load_I80_stations.sql')

create_richards = MySqlOperator(dag=dag,
                           mysql_conn_id='mysql-connect', 
                           task_id='create_richards',
                            sql='create_richards_table.sql')

load_richards = MySqlOperator(dag=dag,
                           mysql_conn_id='mysql-connect', 
                           task_id='load_richards',
                            sql='load_richards.sql')


drop_table = MySqlOperator(dag=dag,
                           mysql_conn_id='mysql-connect', 
                           task_id='drop_table',
                            sql='sample_sql.sql')

create_table >> load_I80_stations >> create_richards >>load_richards >> drop_table