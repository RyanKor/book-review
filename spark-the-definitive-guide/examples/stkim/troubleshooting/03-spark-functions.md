# 개요

1. `Data source write support MicroBatchWrite`

- Spark 스트리밍 실행에서 발생하며, 보통 데이터가 메모리 소스에 쓸 때 문제가 생길 때 발생

```
24/11/03 11:45:14 ERROR WriteToDataSourceV2Exec: Data source write support MicroBatchWrite[epoch: 21, writer: org.apache.spark.sql.execution.streaming.sources.MemoryStreamingWrite@c3fb938] is aborting.
24/11/03 11:45:14 ERROR WriteToDataSourceV2Exec: Data source write support MicroBatchWrite[epoch: 21, writer: org.apache.spark.sql.execution.streaming.sources.MemoryStreamingWrite@c3fb938] aborted.
```