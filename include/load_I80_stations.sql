LOAD DATA LOCAL INFILE  
'/usr/local/airflow/include/I80_stations.csv'
INTO TABLE your_awesome_table  
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n';