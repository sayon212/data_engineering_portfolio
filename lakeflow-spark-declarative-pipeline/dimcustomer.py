from pyspark import pipelines as dp
from pyspark.sql.functions import current_timestamp

cust_schema = "custid INT, cust_name STRING, email STRING, phone STRING"

# read incremental files from landing using autoloader
@dp.table(name="customers_standardized")
@dp.expect_or_drop("valid_fields" , "custid IS NOT NULL")
def customers_standardized():
    df = spark.readStream.format("cloudFiles") \
        .option("cloudFiles.format", "csv") \
        .option("header","true") \
        .schema(cust_schema) \
        .option("cloudFiles.schemaLocation", "/Volumes/workspace/learning/learning_volume/DLT/schemalocation/dimCust/") \
        .option("cloudFiles.schemaEvolutionMode", "none") \
        .load("/Volumes/workspace/learning/learning_volume/DLT/source_files/customer/")

    return df.withColumn("loadtime" , current_timestamp())

# read incremental data from customer standardized table and store as SCD1
dp.create_streaming_table(name="workspace.curated.customer_upserts")
dp.create_auto_cdc_flow(
    target = "workspace.curated.customer_upserts",
    source = "customers_standardized",
    keys = ["custid"],
    sequence_by = "loadtime",
    stored_as_scd_type = 2
)





