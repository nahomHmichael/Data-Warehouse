{{ config(materialized='table') }}

with traffic_model as (

    select * from traffic_raw
)
select *
from traffic_model