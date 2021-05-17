{{ config(
    materialized='view'
) }}

SELECT * FROM example.taxi_zone_lookup
