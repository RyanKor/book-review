from pyspark.sql import SparkSession
from pyspark import SparkConf

# SparkConf 설정 (Docker Compose 환경에 맞춰 마스터 URL 지정)
spark = SparkSession.builder \
    .appName("definitive spark chapter 03 - Streaming API") \
    .master("spark://localhost:7077") \
    .getOrCreate()

# 로깅 수준 설정 (선택 사항)
spark.sparkContext.setLogLevel("ERROR")

# 파티션 수 지정: 기본 값은 200인데 5로 조정.
spark.conf.set('spark.sql.shuffle.partitions', "5")

staticDataFrame = spark.read.format("csv")\
  .option("header", "true")\
  .option("inferSchema", "true")\
  .load("file:///mnt/nvme/dataset/spark/retail-data/by-day/*.csv")

staticDataFrame.createOrReplaceTempView("retail_data")
staticSchema = staticDataFrame.schema


# COMMAND ----------

from pyspark.sql.functions import window, column, desc, col
staticDataFrame\
  .selectExpr(
    "CustomerId",
    "(UnitPrice * Quantity) as total_cost",
    "InvoiceDate")\
  .groupBy(
    col("CustomerId"), window(col("InvoiceDate"), "1 day"))\
  .sum("total_cost")\
  .show(5)

# COMMAND ----------

# 스트리밍 API에서 read -> readStream으로 메서드 대신 사용.
# maxFilesPerTrigger -> 한 번에 읽을 파일 수 지정 가능.
streamingDataFrame = spark.readStream\
    .schema(staticSchema)\
    .option("maxFilesPerTrigger", 1)\
    .format("csv")\
    .option("header", "true")\
    .load("file:///mnt/nvme/dataset/spark/retail-data/by-day/*.csv")

streamingDataFrame.isStreaming

# COMMAND ----------
# 총 판매 금액 계산
# 지연 연산으로 데이터 플로우 계산을 위해 스트리밍 액션 호출.
purchaseByCustomerPerHour = streamingDataFrame\
  .selectExpr(
    "CustomerId",
    "(UnitPrice * Quantity) as total_cost",
    "InvoiceDate")\
  .groupBy(
    col("CustomerId"), window(col("InvoiceDate"), "1 day"))\
  .sum("total_cost")


# COMMAND ----------
# 메모리에 기록
purchaseByCustomerPerHour.writeStream\
    .format("memory")\
    .queryName("customer_purchases")\
    .outputMode("complete")\
    .start()


# COMMAND ----------

spark.sql("""
  SELECT *
  FROM customer_purchases
  ORDER BY `sum(total_cost)` DESC
  """)\
  .show(5)

# 콘솔에 기록
purchaseByCustomerPerHour.writeStream\
    .format("console")\
    .queryName("customer_purchases_2")\
    .outputMode("complete")\
    .start()

# COMMAND ----------

from pyspark.sql.functions import date_format, col
preppedDataFrame = staticDataFrame\
  .na.fill(0)\
  .withColumn("day_of_week", date_format(col("InvoiceDate"), "EEEE"))\
  .coalesce(5)


# COMMAND ----------
# ML을 위한 데이터셋 분리.
trainDataFrame = preppedDataFrame\
  .where("InvoiceDate < '2011-07-01'")
testDataFrame = preppedDataFrame\
  .where("InvoiceDate >= '2011-07-01'")

trainDataFrame.count()
testDataFrame.count()

# COMMAND ----------
# 월 ~ 일을 1 ~7 변환
from pyspark.ml.feature import StringIndexer
indexer = StringIndexer()\
  .setInputCol("day_of_week")\
  .setOutputCol("day_of_week_index")


# COMMAND ----------
# 1, 0으로 요일 인코딩.
from pyspark.ml.feature import OneHotEncoder
encoder = OneHotEncoder()\
  .setInputCol("day_of_week_index")\
  .setOutputCol("day_of_week_encoded")


# COMMAND ----------

from pyspark.ml.feature import VectorAssembler

vectorAssembler = VectorAssembler()\
  .setInputCols(["UnitPrice", "Quantity", "day_of_week_encoded"])\
  .setOutputCol("features")


# COMMAND ----------

from pyspark.ml import Pipeline

transformationPipeline = Pipeline()\
  .setStages([indexer, encoder, vectorAssembler])


# COMMAND ----------

fittedPipeline = transformationPipeline.fit(trainDataFrame)


# COMMAND ----------

transformedTraining = fittedPipeline.transform(trainDataFrame)
transformedTraining.unpersist()
transformedTraining.cache()

# COMMAND ----------

from pyspark.ml.clustering import KMeans
kmeans = KMeans()\
  .setK(20)\
  .setSeed(1)


# COMMAND ----------

kmModel = kmeans.fit(transformedTraining)
kmModel.computeCost(transformedTraining)

# COMMAND ----------

transformedTest = fittedPipeline.transform(testDataFrame)
kmModel.computeCost(transformedTest)


# COMMAND ----------

from pyspark.sql import Row

spark.sparkContext.parallelize([Row(1), Row(2), Row(3)]).toDF()


# COMMAND ----------
