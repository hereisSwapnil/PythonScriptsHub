from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("Complex Data Transformation") \
    .getOrCreate()

# Read CSV file (assuming the file has columns 'col1', 'col2', 'col3')
input_path = "input.csv"
df = spark.read.csv(input_path, header=True, inferSchema=True)

# Perform Complex Transformation
df_transformed = df \
    .withColumn("new_col", col("col1") * 2) \
    .withColumn("new_col2", expr("col2 + 10")) \
    .filter(col("col3") > 5)

# Write the result to a new CSV file
output_path = "output.csv"
df_transformed.write.csv(output_path, header=True, mode="overwrite")

# Stop SparkSession
spark.stop()
