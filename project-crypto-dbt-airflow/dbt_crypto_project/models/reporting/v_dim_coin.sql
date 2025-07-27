{{ config(materialized='view' , schema='report') }}

select * from {{ ref('dim_coin') }}