# 3. 스파크 기능 둘러보기

- 스파크 에코 시스템 구조도

- 얼핏 보기에는 저수준 API를 많이 추상화 시켜서 고수준 API, 그리고 기타 기능들을 구현해 놓은 것으로 보인다.

    - 물론 뒤의 챕터들을 더 봐야겠지만, 이렇게 구성하면 저수준 클래스들에 의존성이 크지 않을까?
    - 그리고 스파크 성능에 지장을 주는 의존성을 놓치는 것은 아닐까?

![image](https://github.com/user-attachments/assets/a6b88f30-d4c4-466e-8b5a-1dfb2729c645)

## 3.1 스파크 운영용 애플리케이션 사용하기

- `spark-sumit`을 사용하면 대화용 셸에서 운영용 애플리케이션으로 쉽게 전환 가능 (아직 사용 안해봄.)
- `spark-sumit`을 사용하면 스탠드 얼론(독립적으로 작동할 수 있는 시스템이나 애플리케이션), 메소드, YARN 애플리케이션에서 사용 가능함.

## 3.2 Dataset API

- 자바, 스칼라의 정적 타이핑 지원을 위해 구성한 클래스로 파이썬, R에서 사용 불가.
    - 특정 언어의 정적 타이핑을 지원한다는 것은 컴파일 시점에 타입의 안정성을 높이는 목적으로 사용하는 것.
    - R은 모르겠지만 파이썬은 `Type Hinting`이 추가되어서 정적 타이핑이 가능한데..? 3.x에서 지원하는가? -> NO!
    - 비공식 모듈을 사용해서 유사하게 구현은 가능하지만, Dataset API로써 사용은 불가능.
        - https://stackoverflow.com/questions/73840095/spark-datasets-available-in-python
    - 다수의 개발자가 잘 정의한 인터페이스로 상호 작용하는 대규모 애플리케이션 개발에 유리함.
- 대체할 수 있는 게 있으니 파이썬 스크립트 환경에서 사용할 수 없음에도 스파크 사용률이 높아졌지 않았을까?

## 3.3 구조적 스트리밍

- 구조적 API로 개발된 배치 모드의 연산을 스트리밍 방식으로 실행

- 데이터가 꾸준히 생성되는 상황 (여기서 "꾸준히"가 실시간은 아닌가?)을 가정하고 예제를 구성함.

- 예제 데이터는 시계열 데이터고, `윈도우 함수`를 사용해서 시계열 컬럼 값 기준으로 전체 데이터를 가지는 윈도우 구성함 (Sliding-Window 알고리즘 같은 것인가?)

- 특정 고객이 대량으로 구매하는 영업 시간대를 조회하는 로직. (일 단위)

- 예제 실행 결과

![example result](https://github.com/user-attachments/assets/e7acb92a-582b-4225-8400-e84bb56ca7cc)

- 스트리밍 액션은 `트리거`가 실행된 뒤, 데이터를 갱신하게 될 인메모리 테이블에 데이터를 저장함.

- 데이터 갱신은 이전 집계값보다 클 때만 이뤄지므로, 집계 값은 항상 가장 큰 값을 얻을 수 있음.

- 이 집계 값을 메모리 또는 콘솔에 기록해 볼 수 있는데, 이 방법은 실제 운영 환경에서 추천하지 않음 (이 책의 좋은점? 운영 환경에 대한 레퍼런스 제공.)

- 여기에 예제에서 스파크가 데이터를 처리하는 시점이 아닌 이벤트 시간에 따른 윈도우 구성이 주목할 부분인데, 기존 스파크 스트리밍의 단점을 구조적 스트리밍으로 보완 가능 (5장에서 지속됨.)

## 3.4 ML 학습
- ML 학습을 위한 데이터 수치화
    - StringIndexer
    - OneHot Encoder
    - VectorAssemble
- 학습 준비 프로세스 2단계
    - 데이터 변환
    - 파이프라인 구성

- 모델 학습 프로세스 2단계

    - 모델 초기화
    - 모델 학습

## 3.5 저수준 API

- RDD: 대부분의 스파크 기능들이 RDD 기반으로 효율적인 분산처리 목적으로 사용됨.

- RDD를 직접 쓰는 것보다 구조적 API 사용 권장.

    - 단, RDD 쓰면 좀 더 세밀한 제어가 가능.

## 후기

- 스파크 관련 레퍼런스를 찾아보던 중, 기본 엔진은 스파크 엔진을 쓰고, SQL 분석 엔진은 Trino를 사용하는 케이스가 꽤 보편적인 것으로 확인됨.

    - https://blue-it-society.tistory.com/6

- 스파크의 확장성 (다양한 플러그인, 에코시스템 호환성)이 무척 좋다.