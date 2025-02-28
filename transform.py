from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr

def process_stream_data():
    spark = SparkSession.builder.appName("RetailETL").getOrCreate()
    
    df = spark.readStream.format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "retail_transactions") \
        .load()
    
    df_transformed = df.selectExpr("CAST(value AS STRING)") \
        .withColumn("total_price", col("quantity") * col("price"))
    
    df_transformed.writeStream \
        .format("parquet") \
        .option("checkpointLocation", "/tmp/checkpoints/") \
        .option("path", "/tmp/transformed_data/") \
        .start()
