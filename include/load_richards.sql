LOAD DATA LOCAL INFILE  
'/usr/local/airflow/include/richards.csv'
INTO TABLE richards  
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n';