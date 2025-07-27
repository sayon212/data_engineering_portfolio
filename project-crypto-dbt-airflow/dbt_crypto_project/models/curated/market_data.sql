{{ config(materialized='table') }}

WITH cleaned_market_data AS ( 
    SELECT 
    id as coin_id, 
    symbol as coin_symbol, 
    "name" as coin_name, 
    image as coin_image, 
    circulating_supply, 
    total_supply, 
    coalesce(max_supply, total_supply) as max_supply,
    ath as all_time_high, 
    atl as all_time_low,
    CURRENT_TIMESTAMP as load_time
    FROM {{ source('raw','market_metrics') }}
)

SELECT * FROM cleaned_market_data
