import time
import os
from pyspark import SparkConf, SparkContext

# Spark 설정
conf = SparkConf().setAppName("DockerComposeSparkPerformanceTest").setMaster("spark://localhost:7077")
sc = SparkContext(conf=conf)

# 데이터 범위
data_range = 1_000_000

# Spark 성능 테스트
spark_start_time = time.time()
numbers = sc.parallelize(range(1, data_range + 1))
total_sum_spark = numbers.reduce(lambda x, y: x + y)
spark_end_time = time.time()
spark_execution_time = spark_end_time - spark_start_time

print("Total sum from 1 to", data_range, "using Spark:", total_sum_spark)
print("Spark execution time:", spark_execution_time, "seconds")

# SparkContext 종료
sc.stop()

# 로컬 성능 테스트
local_start_time = time.time()
total_sum_local = sum(range(1, data_range + 1))
local_end_time = time.time()
local_execution_time = local_end_time - local_start_time

print("Total sum from 1 to", data_range, "using local Python:", total_sum_local)
print("Local execution time:", local_execution_time, "seconds")

# 비교 결과 출력
if spark_execution_time < local_execution_time:
    print(f"Spark is faster by {local_execution_time - spark_execution_time:.2f} seconds.")
else:
    print(f"Local Python is faster by {spark_execution_time - local_execution_time:.2f} seconds.")
