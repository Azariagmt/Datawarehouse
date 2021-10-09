LOAD DATA LOCAL INFILE  
'/usr/local/airflow/include/I80_stations.csv'
INTO TABLE I80_stations  
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n';