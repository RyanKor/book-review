from pyspark.sql import SparkSession, Row
from pyspark import SparkConf
from pyspark.sql.functions import col, split, explode
from pyspark.sql.types import StringType, StructType, StructField, ArrayType


# SparkConf 설정 (메모리와 코어 수 조절)
conf = SparkConf() \
    .setAppName("Spark Study Chapter 12") \
    .setMaster("spark://localhost:7077") \
    .set("spark.executor.memory", "6g") \
    .set("spark.executor.cores", "4") \
    .set("spark.driver.memory", "6g") \
    .set("spark.executor.instances", "5")

# SparkSession 생성
spark = SparkSession.builder.config(conf=conf).getOrCreate()

# 로깅 수준 설정 (선택 사항)
spark.sparkContext.setLogLevel("ERROR")

my_collection = "Spark The Definitive Guide : Big Data Processing Made Simple"\
  .split(" ")
words = spark.sparkContext.parallelize(my_collection, 2)


# COMMAND ----------

supplementalData = {"Spark":1000, "Definitive":200,
                    "Big":-300, "Simple":100}


# COMMAND ----------

suppBroadcast = spark.sparkContext.broadcast(supplementalData)


# COMMAND ----------

suppBroadcast.value


# COMMAND ----------

words.map(lambda word: (word, suppBroadcast.value.get(word, 0)))\
  .sortBy(lambda wordPair: wordPair[1])\
  .collect()


# COMMAND ----------

flights = spark.read\
  .parquet("/mnt/nvme/dataset/spark/flight-data/parquet/2010-summary.parquet")


# COMMAND ----------

accChina = spark.sparkContext.accumulator(0)


# COMMAND ----------

def accChinaFunc(flight_row):
  destination = flight_row["DEST_COUNTRY_NAME"]
  origin = flight_row["ORIGIN_COUNTRY_NAME"]
  if destination == "China":
    accChina.add(flight_row["count"])
  if origin == "China":
    accChina.add(flight_row["count"])


# COMMAND ----------

flights.foreach(lambda flight_row: accChinaFunc(flight_row))


# COMMAND ----------

accChina.value # 953


# COMMAND ----------
