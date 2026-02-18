from pyspark import pipelines as dp
from pyspark.sql.functions import sum

@dp.materialized_view(name="workspace.processed.vw_customer_agg")
def compute_aggregation():
    df_cust = spark.read.table("workspace.curated.customer_upserts").where("__END_AT IS NULL")
    df_txn = spark.read.table("workspace.curated.fact_transactions")
    df_joined = df_txn.join(df_cust, how="left_outer", on=df_cust.custid==df_txn.cust_id).drop(df_cust.custid)
    df_agg = df_joined.groupBy("cust_id","cust_name").agg(sum("order_value").alias("total_order_value"))
    return df_agg

