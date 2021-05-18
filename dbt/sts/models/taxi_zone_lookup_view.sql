{{ config(
    materialized='view'
) }}

select *
from {{ source('source', 'taxi_zone_lookup') }}
