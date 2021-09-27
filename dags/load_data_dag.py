from airflow import DAG
from airflow.operators.mysql_operator import MySqlOperator

default_arg = {'owner': 'airflow', 'start_date': '2020-02-28'}

dag = DAG('load-data',
          default_args=default_arg,
          schedule_interval='@once')

create_table = MySqlOperator(dag=dag,
                           mysql_conn_id='mysql-connect', 
                           task_id='create_table',
                            sql=r"""CREATE TABLE IF NOT EXISTS your_awesome_table(ID int,flow_99 int,flow_max int,flow_median int,flow_total int,n_obs int);""")



load_I80_stations = MySqlOperator(dag=dag,
                           mysql_conn_id='mysql-connect', 
                           task_id='load_stations',
                            sql=r"""LOAD DATA LOCAL INFILE  
                                    '/usr/local/airflow/include/I80_stations.csv'
                                    INTO TABLE your_awesome_table  
                                    FIELDS TERMINATED BY ',' 
                                    ENCLOSED BY '"'
                                    LINES TERMINATED BY '\n';""")

create_richards = MySqlOperator(dag=dag,
                           mysql_conn_id='mysql-connect', 
                           task_id='create_richards',
                            sql=r"""CREATE TABLE IF NOT EXISTS richards(timestamp datetime,flow1 float,	occupancy1 float,flow2 float,occupancy2 float,flow3 float,occupancy3 float,totalflow float,weekday int,	hour int,minute int,second int);""")

load_richards = MySqlOperator(dag=dag,
                           mysql_conn_id='mysql-connect', 
                           task_id='load_richards',
                            sql=r"""LOAD DATA LOCAL INFILE  
                                    '/usr/local/airflow/include/richards.csv'
                                    INTO TABLE richards  
                                    FIELDS TERMINATED BY ',' 
                                    ENCLOSED BY '"'
                                    LINES TERMINATED BY '\n';""")

create_table >> load_I80_stations >> create_richards >>load_richards