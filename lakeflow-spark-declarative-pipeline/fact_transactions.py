from pyspark import pipelines as dp

txn_schema = "invoice_num string , invoice_dttm timestamp, cust_id int , order_value double"

@dp.table(name="transactions_standardized")
def transactions_standardized():
    df = spark.readStream.format("cloudFiles") \
        .option("cloudFiles.format", "csv") \
        .option("header","true") \
        .schema(txn_schema) \
        .option("cloudFiles.schemaLocation", "/Volumes/workspace/learning/learning_volume/DLT/schemalocation/factTxn/") \
        .option("cloudFiles.schemaEvolutionMode", "none") \
        .load("/Volumes/workspace/learning/learning_volume/DLT/source_files/transactions/")
    return df

@dp.table(name="workspace.curated.fact_transactions")
def fact_transactions():
    return spark.read.table("transactions_standardized")


