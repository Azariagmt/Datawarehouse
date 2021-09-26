-- Join of stg_I80_stations and stg_station_summary

-- SELECT * INSERT 
-- INTO {{ref('I80_stations')}} FROM {{ref('station_summary')}};

SELECT I80_stations.ID, 
    I80_stations.Dir,
    I80_stations.Fwy,	
    I80_stations.District,	
    I80_stations.County,
    I80_stations.City,	
    I80_stations.State_PM,
    I80_stations.Abs_PM,	
    I80_stations.Latitude,	
    I80_stations.Longitude,	
    I80_stations.Length,	
    I80_stations.Type,	
    I80_stations.Lanes,	
    I80_stations.Name,	
    I80_stations.User_ID_1,	
    I80_stations.User_ID_2,	
    I80_stations.User_ID_3,	
    I80_stations.User_ID_4,	
    flow_99,	
    flow_max,	
    flow_median,	
    flow_total,
    n_obs
FROM {{ref('I80_stations')}} AS I80_stations
INNER JOIN {{ref('station_summary')}} AS station_summary
ON I80_stations.ID = station_summary.ID