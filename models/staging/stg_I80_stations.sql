-- with source as (
--   select * from {{ ref('I80_stations') }}
-- ),

-- stage_I80_stations as (
--   select
--     ID,	
--     Fwy,	
--     Dir	,
--     District,	
--     County,
--     City,
--     State_PM,	
--     Abs_PM,
--     Latitude,	
--     Longitude,	
--     Length,
--     Type,
--     Lanes,
--     Name,
--     User_ID_1,	
--     User_ID_2,	
--     User_ID_3,	
--     User_ID_4
--   from source
-- )

-- select
--   *
-- from stage_I80_stations

select * from {{ref('I80_stations')}}