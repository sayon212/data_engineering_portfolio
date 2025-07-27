{{ config(materialized='table') }}

WITH cleaned_hist_data AS ( 
    SELECT 
    coin_id,
    price,
    market_cap,
    total_volumes,
    "timestamp" as trading_timestamp,
    CURRENT_TIMESTAMP as load_time
    FROM {{ source('raw','coin_historical') }}
)

SELECT * FROM cleaned_hist_data
