LOAD DATA LOCAL INFILE  
'/usr/local/airflow/include/station_summary.csv'
INTO TABLE station_summary  
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n';