{{ config(materialized='view' , schema='report') }}

select * from {{ ref('fact_coins') }}