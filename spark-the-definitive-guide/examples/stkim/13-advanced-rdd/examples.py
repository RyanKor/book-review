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

myCollection = "Spark The Definitive Guide : Big Data Processing Made Simple"\
  .split(" ")
words = spark.sparkContext.parallelize(myCollection, 2)


# COMMAND ----------

words.map(lambda word: (word.lower(), 1))


# COMMAND ----------

keyword = words.keyBy(lambda word: word.lower()[0])


# COMMAND ----------

keyword.mapValues(lambda word: word.upper()).collect()


# COMMAND ----------

keyword.flatMapValues(lambda word: word.upper()).collect()


# COMMAND ----------

keyword.keys().collect()
keyword.values().collect()


# COMMAND ----------

import random
distinctChars = words.flatMap(lambda word: list(word.lower())).distinct()\
  .collect()
sampleMap = dict(map(lambda c: (c, random.random()), distinctChars))
words.map(lambda word: (word.lower()[0], word))\
  .sampleByKey(True, sampleMap, 6).collect()


# COMMAND ----------

chars = words.flatMap(lambda word: word.lower())
KVcharacters = chars.map(lambda letter: (letter, 1))
def maxFunc(left, right):
  return max(left, right)
def addFunc(left, right):
  return left + right
nums = spark.sparkContext.parallelize(range(1,31), 5)


# COMMAND ----------

KVcharacters.countByKey()


# COMMAND ----------
from functools import reduce
KVcharacters.groupByKey().map(lambda row: (row[0], reduce(addFunc, row[1])))\
  .collect()
# 이 코드는 파이썬2 기준으로 되어 있습니다. 파이썬 3을 사용하는 경우, functools에서 reduce를 임포트 해야 합니다.(역자주: from functools import reduce 구문을 사용합니다.)


# COMMAND ----------

nums.aggregate(0, maxFunc, addFunc)


# COMMAND ----------

depth = 3
nums.treeAggregate(0, maxFunc, addFunc, depth)


# COMMAND ----------

KVcharacters.aggregateByKey(0, addFunc, maxFunc).collect()


# COMMAND ----------

def valToCombiner(value):
  return [value]
def mergeValuesFunc(vals, valToAppend):
  vals.append(valToAppend)
  return vals
def mergeCombinerFunc(vals1, vals2):
  return vals1 + vals2
outputPartitions = 6
KVcharacters\
  .combineByKey(
    valToCombiner,
    mergeValuesFunc,
    mergeCombinerFunc,
    outputPartitions)\
  .collect()


# COMMAND ----------

KVcharacters.foldByKey(0, addFunc).collect()


# COMMAND ----------

import random
distinctChars = words.flatMap(lambda word: word.lower()).distinct()
charRDD = distinctChars.map(lambda c: (c, random.random()))
charRDD2 = distinctChars.map(lambda c: (c, random.random()))
charRDD.cogroup(charRDD2).take(5)


# COMMAND ----------

keyedChars = distinctChars.map(lambda c: (c, random.random()))
outputPartitions = 10
KVcharacters.join(keyedChars).count()
KVcharacters.join(keyedChars, outputPartitions).count()


# COMMAND ----------

numRange = spark.sparkContext.parallelize(range(10), 2)
words.zip(numRange).collect()


# COMMAND ----------

words.coalesce(1).getNumPartitions() # 1


# COMMAND ----------

df = spark.read.option("header", "true").option("inferSchema", "true")\
  .csv("/mnt/nvme/dataset/spark/retail-data/all")
rdd = df.coalesce(10).rdd


# COMMAND ----------

def partitionFunc(key):
  import random
  if key == 17850 or key == 12583:
    return 0
  else:
    return random.randint(1,2)

keyedRDD = rdd.keyBy(lambda row: row[6])
keyedRDD\
  .partitionBy(3, partitionFunc)\
  .map(lambda x: x[0])\
  .glom()\
  .map(lambda x: len(set(x)))\
  .take(5)


# COMMAND ----------
