from pyspark.sql import SparkSession
from pyspark import SparkConf

# SparkConf 설정 (Docker Compose 환경에 맞춰 마스터 URL 지정)
spark = SparkSession.builder \
    .appName("definitive spark chapter 07 - Aggregation") \
    .master("spark://localhost:7077") \
    .getOrCreate()

# 로깅 수준 설정 (선택 사항)
spark.sparkContext.setLogLevel("ERROR")

# coalesce는 파티션 갯수 줄일 때만 사용.
# 셔플이 반드시 동반되지 않는 기능임.
# 여기서 파티션 수를 줄이는 이유는 적은 양의 데이터를 가진 수많은 파일이 있기 때문.
df = spark.read.format("csv")\
  .option("header", "true")\
  .option("inferSchema", "true")\
  .load("/mnt/nvme/dataset/spark/retail-data/all/*.csv")\
  .coalesce(5)
df.cache()
df.createOrReplaceTempView("dfTable")


# COMMAND ----------
# count는 트랜스포메이션이 아닌 액션 -> 스파크에게 연산하라고 명령하는 것.
from pyspark.sql.functions import count
df.select(count("StockCode")).show() # 541909


# COMMAND ----------

from pyspark.sql.functions import countDistinct
df.select(countDistinct("StockCode")).show() # 4070


# COMMAND ----------

from pyspark.sql.functions import approx_count_distinct
df.select(approx_count_distinct("StockCode", 0.1)).show() # 3364


# COMMAND ----------

from pyspark.sql.functions import first, last
df.select(first("StockCode"), last("StockCode")).show()


# COMMAND ----------

from pyspark.sql.functions import min, max
df.select(min("Quantity"), max("Quantity")).show()


# COMMAND ----------

from pyspark.sql.functions import sum
df.select(sum("Quantity")).show() # 5176450


# COMMAND ----------

from pyspark.sql.functions import sumDistinct
df.select(sumDistinct("Quantity")).show() # 29310


# COMMAND ----------

from pyspark.sql.functions import sum, count, avg, expr

df.select(
    count("Quantity").alias("total_transactions"),
    sum("Quantity").alias("total_purchases"),
    avg("Quantity").alias("avg_purchases"),
    expr("mean(Quantity)").alias("mean_purchases"))\
  .selectExpr(
    "total_purchases/total_transactions",
    "avg_purchases",
    "mean_purchases").show()


# COMMAND ----------

from pyspark.sql.functions import var_pop, stddev_pop
from pyspark.sql.functions import var_samp, stddev_samp
df.select(var_pop("Quantity"), var_samp("Quantity"),
  stddev_pop("Quantity"), stddev_samp("Quantity")).show()


# COMMAND ----------

from pyspark.sql.functions import skewness, kurtosis
df.select(skewness("Quantity"), kurtosis("Quantity")).show()


# COMMAND ----------

from pyspark.sql.functions import corr, covar_pop, covar_samp
df.select(corr("InvoiceNo", "Quantity"), covar_samp("InvoiceNo", "Quantity"),
    covar_pop("InvoiceNo", "Quantity")).show()


# COMMAND ----------

from pyspark.sql.functions import collect_set, collect_list
df.agg(collect_set("Country"), collect_list("Country")).show()


# COMMAND ----------

from pyspark.sql.functions import count

df.groupBy("InvoiceNo").agg(
    count("Quantity").alias("quan"),
    expr("count(Quantity)")).show()


# COMMAND ----------

df.groupBy("InvoiceNo").agg(expr("avg(Quantity)"),expr("stddev_pop(Quantity)"))\
  .show()


# COMMAND ----------

from pyspark.sql.functions import col, to_date
dfWithDate = df.withColumn("date", to_date(col("InvoiceDate"), "MM/d/yyyy H:mm"))
dfWithDate.createOrReplaceTempView("dfWithDate")


# COMMAND ----------

from pyspark.sql.window import Window
from pyspark.sql.functions import desc
windowSpec = Window\
  .partitionBy("CustomerId", "date")\
  .orderBy(desc("Quantity"))\
  .rowsBetween(Window.unboundedPreceding, Window.currentRow)


# COMMAND ----------

from pyspark.sql.functions import max
maxPurchaseQuantity = max(col("Quantity")).over(windowSpec)


# COMMAND ----------

from pyspark.sql.functions import dense_rank, rank
purchaseDenseRank = dense_rank().over(windowSpec)
purchaseRank = rank().over(windowSpec)


# COMMAND ----------

from pyspark.sql.functions import col
# spark 3.0 이상에서 시간 데이터 처리 방식이 바뀌어서, 책 버전과 호환이 안되는 이슈가 존재함.
spark.conf.set("spark.sql.legacy.timeParserPolicy", "LEGACY")

dfWithDate.where("CustomerId IS NOT NULL").orderBy("CustomerId")\
  .select(
    col("CustomerId"),
    col("date"),
    col("Quantity"),
    purchaseRank.alias("quantityRank"),
    purchaseDenseRank.alias("quantityDenseRank"),
    maxPurchaseQuantity.alias("maxPurchaseQuantity")).show()


# COMMAND ----------

dfNoNull = dfWithDate.drop()
dfNoNull.createOrReplaceTempView("dfNoNull")


# COMMAND ----------

rolledUpDF = dfNoNull.rollup("Date", "Country").agg(sum("Quantity"))\
  .selectExpr("Date", "Country", "`sum(Quantity)` as total_quantity")\
  .orderBy("Date")
rolledUpDF.show()


# COMMAND ----------

from pyspark.sql.functions import sum

dfNoNull.cube("Date", "Country").agg(sum(col("Quantity")))\
  .select("Date", "Country", "sum(Quantity)").orderBy("Date").show()


# COMMAND ----------

pivoted = dfWithDate.groupBy("date").pivot("Country").sum()


# UDAF는 자바 & 스칼라에서만 사용하기에 예제 없음.
