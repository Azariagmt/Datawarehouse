CREATE TABLE IF NOT EXISTS richards(
    timestamp datetime,
    flow1 float,
	occupancy1 float,
    flow2 float,
    occupancy2 float,
    flow3 float,
    occupancy3 float,
    totalflow float,
    weekday int,	
    hour int,
    minute int,
    second int);