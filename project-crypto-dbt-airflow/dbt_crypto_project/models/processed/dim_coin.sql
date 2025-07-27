{{ config(materialized='table' , schema='pro' , 
    post_hook = ["alter table {{ this }} add primary key (coin_id)"]) 
}}

with coin_data as (
    select 
    row_number() over(order by m.coin_id) as dim_coin_key,
    m.coin_id,
    m.coin_symbol,
    m.coin_name,
    m.total_supply,
    h.price as latest_trading_price,
    h.trading_timestamp as latest_trading_time,
    row_number() over (partition by m.coin_id order by h.trading_timestamp desc) as rnk
    from {{ ref('market_data') }} m
    left join {{ ref('historical_data') }} h on m.coin_id = h.coin_id
)

select 
dim_coin_key,
coin_id ,
coin_symbol ,
coin_name ,
total_supply ,
latest_trading_price ,
latest_trading_time 
from coin_data where rnk=1

