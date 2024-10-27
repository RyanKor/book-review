# 개요

## 1. Conflict between Local python and bitnami spark container python version

```
pyspark.errors.exceptions.base.PySparkRuntimeError: [PYTHON_VERSION_MISMATCH] Python in worker has different version (3, 12) than that in driver 3.11, PySpark cannot run with different minor versions. 
Please check environment variables PYSPARK_PYTHON and PYSPARK_DRIVER_PYTHON are correctly set.
```

### How to solve?

- The current version of bitnami container is 3.5.3, which is using python 3.12
- My desktop is using 3.11, thus it makes conflicts.
- Change container version to 3.5.1. It using python 3.11.9
- Resolved :)

## 2. Conflict between Serial version UID

```
Caused by: java.io.InvalidClassException: org.apache.spark.scheduler.Task; local class incompatible: stream classdesc serialVersionUID = -6188971942555435033, local class serialVersionUID = 553100815431272095
	at java.base/java.io.ObjectStreamClass.initNonProxy(ObjectStreamClass.java:597)
	at java.base/java.io.ObjectInputStream.readNonProxyDesc(ObjectInputStream.java:2051)
	at java.base/java.io.ObjectInputStream.readClassDesc(ObjectInputStream.java:1898)
	at java.base/java.io.ObjectInputStream.readNonProxyDesc(ObjectInputStream.java:2051)
	at java.base/java.io.ObjectInputStream.readClassDesc(ObjectInputStream.java:1898)
	at java.base/java.io.ObjectInputStream.readOrdinaryObject(ObjectInputStream.java:2224)
	at java.base/java.io.ObjectInputStream.readObject0(ObjectInputStream.java:1733)
	at java.base/java.io.ObjectInputStream.readObject(ObjectInputStream.java:509)
	at java.base/java.io.ObjectInputStream.readObject(ObjectInputStream.java:467)
	at org.apache.spark.serializer.JavaDeserializationStream.readObject(JavaSerializer.scala:87)
	at org.apache.spark.serializer.JavaSerializerInstance.deserialize(JavaSerializer.scala:129)
	at org.apache.spark.executor.Executor$TaskRunner.run(Executor.scala:579)
	at java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1136)
	at java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:635)
	at java.base/java.lang.Thread.run(Thread.java:840)
```

### How to solve?

- pyspark version I installed is 3.5.3, but the spark version inside docker is 3.5.1. It result in conflicts.
- Therefore, I have uninstalled pyspark and reinstalled it to 3.5.1.
- see `requirements.txt`