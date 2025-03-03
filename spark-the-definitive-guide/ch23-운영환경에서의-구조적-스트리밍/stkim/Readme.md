# Ch23. 운영환경에서의 구조적 스트리밍

## 23.1 내고장성과 체크포인팅

- 실수로 스키마가 변경될 수도 있고, 클러스터 or 애플리케이션 재시작이 필요할 수도 있음.

    - 구조적 스트리밍이 이런 장애 상황을 극복하게 지원함.

        - 체크포인트, WAL 사용

## 23.2 애플리케이션 변경하기

- 체크포인팅을 사용하면 현재까지 처리한 스트림과 중간 상태를 모두 저장함.

### 23.2.1 스트리밍 애플리케이션 코드 업데이트하기

- 구조적 스트리밍 자체가 애플리케이션 다시 시작하기 전에 특정 유형의 애플리케이션 코드를 변경할 수 있도록 설계가 되어 있음.

- 특히 버그 등 수정 작업을 스파크 사용 중에 수행할 수 있다는 것이 매우 큰 장점.

    - 새로운 집계 키를 추가하거나 쿼리를 완전히 변경하는 등의 업데이트 상황.

### 23.2.2 스파크 버전 업데이트하기

- 구조적 스트리밍에서 과거 버전의 체크포인트를 스파크 버전을 올렸을 때 그대로 사용할 수 있음.

- 그럼에도 릴리즈 노트를 확인해서 스파크 버전 올릴 때 호환성 보장을 꼭 확인하자 (치명적 버그를 수정한 업그레이드 버전은 과거 버전 체크포인트도 실행 안되게 할 수 있음)

### 23.2.3 애플리케이션의 초기 규모 산정과 재조정하기

- 데이터 유입률 > 스파크 데이터 처리량 : 클러스터 또는 애플리케이션 증설 필요.

- 그러나 클러스터 및 애플리케이션 증설은 기본적으로 스파크 클러스터 내에서 셔플을 발생시켜 데이터 재분배를 일으키므로 초기에 연산 지연 이슈가 발생함.

## 23.3 메트릭과 모니터링

- 스트리밍 쿼리 & 최근 실행 작업에 대한 진행 상황 조회 API 제공

### 23.3.1 쿼리 상태

- `query.status` 로 조회 가능함.

### 23.3.2 최근 진행 상황.

- `query.recentProgress` 명령어로 처리율, 배치 주기 등 시간 기반의 정보 확인.

- 출력 정보 자체가 특정 시점의 스냅샷임.

#### 유입률과 처리율

- 유입률이 처리율보다 월등하게 높으면 어쩔 수 없이 클러스터 & 애플리케이션을 증설해야함.

#### 배치 주기

- 구조적 스트리밍은 적절한 시스템 처리량을 유지할 수 있으면서 일정 수준의 응답 속도를 유지할 수 있는 옵션이 있음.

### 23.3.3 스파크 UI

- UI 내에서 실행된 Job 누적되서 기록됨.

## 23.4 알림

- 프로메테우스 등 모니터링 시스템에 메트릭 보내거나 로그 단위로 기록해서 Splunk 같은 로그 집계 시스템 사용해서 분석 가능함.

## 23.5 스트리밍 리스너를 사용한 고급 모니터링

- 더 강력하게 모니터링할 수 있는 방법으로 `StreamingQueryListener` 클래스가 있음

- `StreamingQueryListener` 구현 정도에 따라 모든 쿼리 진행 상황을 카프카에 전송할 수 있음.