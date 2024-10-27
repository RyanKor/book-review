from pyspark.sql import SparkSession
from pyspark import SparkConf

# SparkConf 설정 (Docker Compose 환경에 맞춰 마스터 URL 지정)
conf = SparkConf() \
    .setAppName("DockerComposeSparkPerformanceTest") \
    .setMaster("spark://localhost:7077")

# SparkSession 생성
spark = SparkSession.builder \
    .config(conf=conf) \
    .getOrCreate()

flightData2015 = spark\
  .read\
  .option("inferSchema", "true")\
  .option("header", "true")\
  .csv("/mnt/nvme/Workspace/book-review/spark-the-definitive-guide/examples/stkim/02-spark-example/2015-summary.csv")

# 데이터 미리보기
flightData2015.show()

# SparkSession 종료
spark.stop()