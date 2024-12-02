# RDD

- 스파크의 저수준 API: RDD, SparkContext, Accumulator, broadcast variable과 같은 분산형 공유 변수 등을 의미함.

## 1. 저수준 API란

- 분산 데이터 처리의 RDD

- 공유 변수를 배포하고 다루기 위한 API인 브로드캐스트 & 어큐물레이터

### 1.1 저수준 API는 언제 사용할까

- 고수준 API에서 제공하지 않는 기능을 필요로 할 때 : 아주 세밀한 데이터 배치 등

- RDD를 사용해 개발된 기존 코드 유지 & 보수

- 사용자 정의 공유 변수 다룰 때

- 스파크에 대해 잘 이해하고 있는 개발자라도 구조적 API 기반으로 사용하는 게 좋음.

    - 저수준 API 를 사용해야하는 예시: 이전 버전 스파크에서 자체 구현한 파티셔너를 사용해 데이터 파이프라인 실행 동안 변수 값 갱신하고 추적하는 저수준 API 필요.

### 1.2 저수준 API는 어떻게 사용할까?

- SparkContext는 저수준 API 기능 사용을 위한 진입 지점임.
- SparkSession이 SparkContext로 접근해서 사용함.

## 2. RDD 개요

### 2.1 RDD 유형

### 2.2 RDD는 언제 사용할까

### 2.3 Dataset과 RDD의 케이스 클래스

## 3. RDD 생성하기

### 3.1 DataFrame, Dataset으로 RDD 생성하기

### 3.2 로컬 컬렉션으로 RDD 생성하기

### 3.3 데이터소스로 RDD 생성하기

## 4. RDD 다루기

## 5. 트랜스포메이션

### 5.1 distinct

### 5.2 filter

### 5.3 map

### 5.4 flatMap

### 5.5 sortBy

### 5.6 randomSplit

## 6. 액션

### 6.1 reduce

### 6.2 count

- countApprox
- countApproxDistinct
- countByValue
- countByValueApprox

### 6.3 first

### 6.4 max & min

### 6.5 take

## 7. 파일 저장하기

### 7.1 saveAsTextFile

### 7.2 시퀀스 파일

### 7.3 하둡 파일

## 8. 캐싱

## 9. 체크 포인팅

## 10. RDD를 시스템 명령으로 전송하기

### 10.1 mapPartitions

### 10.2 foreachPartition

### 10.3 glom