{{ config(materialized='incremental') }}

select *
from {{ ref('taxi_zone_lookup_view') }}

{% if is_incremental() %}

  -- this filter will only be applied on an incremental run
  where locationid='23'

{% endif %}

