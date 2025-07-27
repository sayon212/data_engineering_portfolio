{{ config(materialized = 'table', schema = 'pro') }}

with dates as (
    select
        generate_series(
            (select min(trading_timestamp)::date from {{ ref('historical_data') }}),
            (select max(trading_timestamp)::date from {{ ref('historical_data') }}),
            interval '1 day'
        ) as date_day
)
select
    row_number() over (order by date_day) as date_id,
    date_day,
    extract(year from date_day) as year,
    extract(month from date_day) as month,
    to_char(date_day, 'Month') as month_name,
    extract(day from date_day) as day,
    extract(dow from date_day) as day_of_week,
    case when extract(dow from date_day) in (0,6) then true else false end as is_weekend
from dates