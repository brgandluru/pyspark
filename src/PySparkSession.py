from pyspark.sql import SparkSession
spark=SparkSession.builder.appName('PySparkSession').getOrCreate()
data2 = [{"Name": "Alice", "Age": 25}, {"Name": "Bob", "Age": 30}, {"Name": "Charlie", "Age": 28}]
df2 = spark.createDataFrame(data2)
df2.printSchema()
df2.show()