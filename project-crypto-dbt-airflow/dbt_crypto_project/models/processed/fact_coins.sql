{{ config(materialized='incremental' , schema='pro' , unique_key = 'fact_key') }}

with fact_coins as (
    select 
    md5(concat_ws('||',c.coin_id,h.trading_timestamp,h.price)) as fact_key,
    c.coin_id,
    h.price as days_price,
    h.total_volumes,
    h.trading_timestamp,
    dt.date_id
    from {{ ref('historical_data') }} h
    left join {{ ref('dim_coin') }} c on c.coin_id = h.coin_id
    left join {{ ref('dim_date') }} dt on h.trading_timestamp::date = dt.date_day::date
    )

select * from fact_coins

{% if is_incremental() %}
    where trading_timestamp > (select max(trading_timestamp) from {{ this }})
{% endif %}