# 개요

## 1. Local File Path Not Found Error accessing mounted dataset directory

```
flightData2015 = spark\
  .read\
  .option("inferSchema", "true")\
  .option("header", "true")\
  .csv('file:///mnt/nvme/dataset/spark/2015-summary.csv')
```

### How to solve?

- The mounted path has to be matched with the local path.
- Which means the path spark driver and executor access have been to find the same path in their environment.

```bash
# spark-master, spark-worker-1, spark-worker-2
volumes:
	- /mnt/nvme/dataset/spark:/mnt/nvme/dataset/spark
```
