from pyspark.sql import SparkSession
from pyspark import SparkConf

# SparkConf 설정 (Docker Compose 환경에 맞춰 마스터 URL 지정)
spark = SparkSession.builder \
    .appName("definitive spark chapter 04 - Structural API") \
    .master("spark://localhost:7077") \
    .getOrCreate()

# 로깅 수준 설정 (선택 사항)
spark.sparkContext.setLogLevel("ERROR")


df = spark.range(500).toDF("number")
df.select(df["number"] + 10)


# COMMAND ----------

spark.range(2).collect()


# COMMAND ----------

from pyspark.sql.types import *
b = ByteType()


# COMMAND ----------
