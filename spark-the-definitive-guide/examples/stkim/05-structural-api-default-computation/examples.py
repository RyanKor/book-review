from pyspark.sql import SparkSession
from pyspark import SparkConf

# SparkConf 설정 (Docker Compose 환경에 맞춰 마스터 URL 지정)
spark = SparkSession.builder \
    .appName("definitive spark chapter 05 - Structural API Default Computation") \
    .master("spark://localhost:7077") \
    .getOrCreate()

# 로깅 수준 설정 (선택 사항)
spark.sparkContext.setLogLevel("ERROR")

df = spark.read.format("json").load("/mnt/nvme/dataset/spark/flight-data/json/2015-summary.json")


# 스키마 조회하기

spark.read.format("json").load("/mnt/nvme/dataset/spark/flight-data/json/2015-summary.json").schema


# 컬럼의 기본 데이터 타입은 StructType임.

from pyspark.sql.types import StructField, StructType, StringType, LongType

myManualSchema = StructType([
  StructField("DEST_COUNTRY_NAME", StringType(), True),
  StructField("ORIGIN_COUNTRY_NAME", StringType(), True),
  StructField("count", LongType(), False, metadata={"hello":"world"})
])
df = spark.read.format("json").schema(myManualSchema)\
  .load("/mnt/nvme/dataset/spark/flight-data/json/2015-summary.json")


# col 메서드로 컬럼 참조 가능.

from pyspark.sql.functions import col, column
col("someColumnName")
column("someColumnName")


# 표현식으로 컬럼 표현하기

from pyspark.sql.functions import expr
expr("(((someCol + 5) * 200) - 6) < otherCol")


# 로우 생성하기

from pyspark.sql import Row
myRow = Row("Hello", None, 1, False)


# 생성한 로우 조회

myRow[0]
myRow[2]


# DataFrame 생성 1

df = spark.read.format("json").load("/mnt/nvme/dataset/spark/flight-data/json/2015-summary.json")
df.createOrReplaceTempView("dfTable")


# DataFrame 생성 2

from pyspark.sql import Row
from pyspark.sql.types import StructField, StructType, StringType, LongType
myManualSchema = StructType([
  StructField("some", StringType(), True),
  StructField("col", StringType(), True),
  StructField("names", LongType(), False)
])
myRow = Row("Hello", None, 1)
myDf = spark.createDataFrame([myRow], myManualSchema)
myDf.show()


# select 메서드 사용해서 SQL을 스파크에서 이용하기.

df.select("DEST_COUNTRY_NAME").show(2)


# 여러 컬럼을 select 메서드 사용해서 확인하기

df.select("DEST_COUNTRY_NAME", "ORIGIN_COUNTRY_NAME").show(2)


# 표현식, col, column을 섞어가면서 select 메서드 사용 가능 

from pyspark.sql.functions import expr, col, column
df.select(
    expr("DEST_COUNTRY_NAME"),
    col("DEST_COUNTRY_NAME"),
    column("DEST_COUNTRY_NAME"))\
  .show(2)


# COMMAND ----------

df.select(expr("DEST_COUNTRY_NAME AS destination")).show(2)


# COMMAND ----------

df.select(expr("DEST_COUNTRY_NAME as destination").alias("DEST_COUNTRY_NAME"))\
  .show(2)


# COMMAND ----------

df.selectExpr("DEST_COUNTRY_NAME as newColumnName", "DEST_COUNTRY_NAME").show(2)


# COMMAND ----------

df.selectExpr(
  "*", # all original columns
  "(DEST_COUNTRY_NAME = ORIGIN_COUNTRY_NAME) as withinCountry")\
  .show(2)


# COMMAND ----------

df.selectExpr("avg(count)", "count(distinct(DEST_COUNTRY_NAME))").show(2)


# 스파크 데이터 타입으로 변환하기

from pyspark.sql.functions import lit
df.select(expr("*"), lit(1).alias("One")).show(2)


# 컬럼의 데이터 타입 변경하기

df.withColumn("numberOne", lit(1)).show(2)


# COMMAND ----------

df.withColumn("withinCountry", expr("ORIGIN_COUNTRY_NAME == DEST_COUNTRY_NAME"))\
  .show(2)


# COMMAND ----------

df.withColumnRenamed("DEST_COUNTRY_NAME", "dest").columns


# COMMAND ----------

dfWithLongColName = df.withColumn(
    "This Long Column-Name",
    expr("ORIGIN_COUNTRY_NAME"))


# COMMAND ----------

dfWithLongColName.selectExpr(
    "`This Long Column-Name`",
    "`This Long Column-Name` as `new col`")\
  .show(2)


# COMMAND ----------

dfWithLongColName.select(expr("`This Long Column-Name`")).columns


# COMMAND ----------

df.where(col("count") < 2).where(col("ORIGIN_COUNTRY_NAME") != "Croatia")\
  .show(2)


# COMMAND ----------

df.select("ORIGIN_COUNTRY_NAME", "DEST_COUNTRY_NAME").distinct().count()


# COMMAND ----------

df.select("ORIGIN_COUNTRY_NAME").distinct().count()


# 로우에서 무작위 샘플 얻기.

seed = 5
withReplacement = False
fraction = 0.5
df.sample(withReplacement, fraction, seed).count()


# COMMAND ----------

dataFrames = df.randomSplit([0.25, 0.75], seed)
dataFrames[0].count() > dataFrames[1].count() # False


# COMMAND ----------

from pyspark.sql import Row
schema = df.schema
newRows = [
  Row("New Country", "Other Country", 5),
  Row("New Country 2", "Other Country 3", 1)
]
parallelizedRows = spark.sparkContext.parallelize(newRows)
newDF = spark.createDataFrame(parallelizedRows, schema)


# 로우 합치기와 추가하기

df.union(newDF)\
  .where("count = 1")\
  .where(col("ORIGIN_COUNTRY_NAME") != "United States")\
  .show()


# COMMAND ----------

df.sort("count").show(5)
df.orderBy("count", "DEST_COUNTRY_NAME").show(5)
df.orderBy(col("count"), col("DEST_COUNTRY_NAME")).show(5)


# COMMAND ----------

from pyspark.sql.functions import desc, asc
df.orderBy(expr("count desc")).show(2)
df.orderBy(col("count").desc(), col("DEST_COUNTRY_NAME").asc()).show(2)


# 트랜스포메이션 실행 전, 파티션을 정렬해서 최적화하는 시도를 수행할 수 있음 -> sortWithPartitions

spark.read.format("json").load("/mnt/nvme/dataset/spark/flight-data/json/*-summary.json")\
  .sortWithinPartitions("count")


# COMMAND ----------

df.limit(5).show()


# COMMAND ----------

df.orderBy(expr("count desc")).limit(6).show()


# COMMAND ----------

df.rdd.getNumPartitions() # 1


# COMMAND ----------

df.repartition(5)


# 특정 칼럼을 기반으로 리파티셔닝 -> 자주 필터로 사용하는 컬럼을 기준으로 파티션을 재구성하면 연산 속도가 빨라짐. 자주 사용하는 컬럼 필터일수록 효과가 큼.

# coalesce vs repartition

# coalesce : 파티션 갯수 줄일 때 사용.

# repartition : 셔플 및 미래에 데이터가 늘어날 것을 감안해서 사용.

df.repartition(col("DEST_COUNTRY_NAME"))


# COMMAND ----------

df.repartition(5, col("DEST_COUNTRY_NAME"))


# COMMAND ----------

df.repartition(5, col("DEST_COUNTRY_NAME")).coalesce(2)


# COMMAND ----------

collectDF = df.limit(10)
collectDF.take(5) # take works with an Integer count
collectDF.show() # this prints it out nicely
collectDF.show(5, False)
collectDF.collect()


# COMMAND ----------
