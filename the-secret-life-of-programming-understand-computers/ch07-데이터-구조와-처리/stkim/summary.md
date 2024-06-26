# CH07 데이터 구조와 처리

# 기본 데이터 타입

> ### 기본 데이터 타입
>
> 기본 데이터 타입은 `primitive data type`(원시 타입)이라고 불린다.

`C언어의 기본타입`:

- char, short, long
- long long
- unsigned char, unsigned short, unsigned long
- unsigned long long
- float
- double
- int
- unsigned int
- 포인터

unsigned는 부호가 없음(양수만 표현), signed는 부호를 표현(음수 ~ 양수)

`Javascript의 기본타입`:

- null
- undefined
- boolean
- number
- string
- symbol(ES2015)
- bigint(ES2020, Number.MAX_SAFE_INTEGER 이상의 숫자 사용 가능)

> ### `포인터`

`포인터`는 64비트 컴퓨터에서 사용되는데, '주소 지정 모드'절에서의 간접 주소 지정이 바로 `포인터`다. 값이 0, 즉 NULL은 일반적으로 제대로 된 주소로 인정하지 않는다.

```
"포인터는 마녀다. 하지만 포인터를 이해하면 마녀의 힘을 쓸 수 있다."
"전자공학, 컴퓨터 전공은 1학년 때 포인터를 잘 넘어가냐 아니냐에 따라 남은 학점이 결정된다."
```

포인터는 C가 인기를 끌면서 유명세를 탔다. 하지만 16비트에서 32비트로 전환이 되고 1970~1980년대 작성된 코드 중 상당수는 포인터를 무신경하게 사용. 예를 들어 포인터와 정수가 같은 크기라고 가정하고 둘을 서로 바꿔 쓰는 경우가 많았음.

새로 등장한 아키텍처로 이런 코드로 포팅하면 프로그램이 깨지거나 디버깅하기 어려운 방식이 되는 경우가 잦음.

이러한 문제를 해결하기 위해 두 가지 독립적인 접근 방법이 생겨남.

- `첫째`로, 이식성에 더 많은 관심을 기울임
- `둘째`로, 자바처럼 포인터를 아예 없앤 언어가 생겨남.

오늘날에 많은 언어들이 포인터를 몰라도 프로그래밍이 가능하도록 만들어져있지만
언어가 동작하는 많은 부분에서 포인터들이 작동하고 있다.

<br>

> ### 참고

- [Javascript의 타입과 자료구조](https://developer.mozilla.org/ko/docs/Web/JavaScript/Data_structures)
- [포인터 - 나무위키](https://namu.wiki/w/%ED%8F%AC%EC%9D%B8%ED%84%B0)
- [포인터 사용이유](https://oper6210.tistory.com/160)

# 배열

> ### 배열
>
> 데이터 구조는 주소와 값을 연관시킨 형태로 아주 단순했다.
> 프로그래밍 언어를 지원하는 배열은 마치 아파트의 형태와 같다.

아파트 한 동에는 주소가 있고, 한 아파트 동 안의 각 집에는 번호(호수)가 있다. 프로그래머는 호수를 `인덱스(index)`라고 부르고 각각의 집을 `원소`라고 부른다.

<img width="400" alt="image" src="https://user-images.githubusercontent.com/91880235/176982809-80b48039-71a2-4198-8582-bc9ef166b7b7.png">

각 층에는 8비트(바이트)가 2개씩 들어있다.

각 원소는 0번째 원소의 주소인 `기저 주소(base address)`로부터 얼마나 멀리 떨어져 있는지를 나타내는 오프셋으로 지정할 수 있다.

프로그래밍 언어는 `다차원 배열`을 지원하며 아래와 같이 차원을 높일 수 있다.

- 3차원 배열: 동, 층, 호수
- 4차원 배열: 단지, 동, 층, 호수
- 5차원 배열: 아파트 이름, 단지, 동, 층, 호수

<br>

> ### 참조 지역성의 문제.
>
> `참조지역성`: 동일한 값 또는 해당 값에 관계된 스토리지 위치가 자주 액세스되는 특성으로, 지역성의 원리(principle of locality)라고도 불림

주소 공간상에서는 열 인덱스가 바뀔 때보다 행 인덱스가 바뀔 때 더 많은 이동이 일어난다.
(배열은 메모리에 연속적인 공간에 저장되기 때문)

- 열 인덱스 이동 (1바이트씩 이동)
- 행 인덱스 이동 (3바이트씩 이동 - 그림 7-3 기준)

전단지를 돌린다는 가정 하에 한 층을 다 돈 다음 다음 층으로 옮기는 게 <u>지역성이 좋고 힘도 덜 든다.</u>

<img width="400" alt="image" src="https://user-images.githubusercontent.com/91880235/176982817-8baa1f53-a27e-4a28-8b2e-839bf248d371.png">

7-2 그림으로 가서 만약 원소10에 접근하려고 한다면 파스칼 같은 프로그래밍 언어는 배열 인덱스 범위를 벗어나지 않는 지 검사한다.

<br>

> ### 자바스크립트 배열은 배열이 아니다?

```
일반적으로 배열이라는 자료 구조의 개념은 동일한 크기의 메모리 공간이 빈틈없이 연속적으로 나열된 자료 구조를 말한다.

즉, 배열의 요소는 하나의 타입으로 통일되어 있으며 서로 연속적으로 인접해 있다. 이러한 배열을 밀집 배열(dense array)이라 한다.
```

<img width="460" alt="image" src="https://user-images.githubusercontent.com/91880235/176983333-2cde3abd-341f-4b36-9d79-bccc6805ad91.png">

배열의 요소를 위한 각각의 메모리 공간은 동일한 크기를 갖지 않아도 되며 연속적으로 이어져 있지 않을 수도 있다. 배열의 요소가 연속적으로 이어져 있지 않는 배열을 희소 배열(sparse array)이라 한다.

이처럼 자바스크립트의 배열은 엄밀히 말해 일반적 의미의 배열이 아니다. 자바스크립트의 배열은 일반적인 배열의 동작을 흉내낸 특수한 객체이다.

그렇기에 자바스크립트에서 사용할 수 있는 모든 값은 객체의 프로퍼티 값이 될 수 있으므로 어떤 타입의 값이라도 배열의 요소가 될 수 있다.

```js
console.log(Object.getOwnPropertyDescriptors([1, 2, 3]));
/*
{
  '0': { value: 1, writable: true, enumerable: true, configurable: true },
  '1': { value: 2, writable: true, enumerable: true, configurable: true },
  '2': { value: 3, writable: true, enumerable: true, configurable: true },
  length: { value: 3, writable: true, enumerable: false, configurable: false }
}
*/

// array[array.length - 1] => arr.at(-1)로 대신 할 수 있음
```

<br>

> ### 일반적인 배열과 자바스크립트 배열과의 차이점

- 일반적인 배열은 인덱스로 배열 요소에 빠르게 접근할 수 있지만
  특정 요소를 탐색하거나 요소를 삽입 또는 삭제하는 경우에는 효율적이지 않다.
  (연속적인 할당 구조)

- JS 배열은 인덱스로 배열 요소에 접근하는 경우 일반 배열보다 느리지만, 특정 요소 탐색, 삽입 또는 삭제하는 경우 일반적인 배열보다 빠르다. (비선형적인 할당 구조)

<br>

> ### 참고

- [[Javascript] 배열 선언, 초기화의 모든 것 (Hacks for Creating Javascript Arrays)](https://cider.tistory.com/2)
- [개발자를 꿈꾸는 프로그래머:티스토리](https://jwprogramming.tistory.com/18)
- [자바스크립트 배열은 배열이 아니다](https://poiemaweb.com/js-array-is-not-arrray)
- [자바스크립트의 배열을 사용할 때 주의할 점](https://velog.io/@yukyung/%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8%EC%9D%98-%EB%B0%B0%EC%97%B4)

# 비트맵

비트의 배열을 `비트맵`이라고 한다.

> 비트맵(영어: BMP file format, DIB file format 또는 bitmap, 문화어: 비트매프, 이진 숫자 배렬표)은 컴퓨터 분야에서 디지털 이미지를 저장하는 데 쓰이는 이미지 파일 포맷 또는 메모리 저장 방식의 한 형태이다.

![그림 7-4 배열을 비트맵으로 생각하기](https://media.discordapp.net/attachments/879215554379018243/992792551125954721/unknown.png)

8로 나누어서 특정 비트가 들어있는 바이트를 찾을 수 있다. `배럴 시프터`가 있으면 `3비트 오른쪽 시프트` 함으로서 빠르게 계산할 수 있다.
ex) 비트 번호가 17이면, 17/8 = 2이므로 2번째 바이트에서 비트를 찾을 수 있다.
<br />

**마스크**
'들여다볼 수 있는' 구멍이 있는 비트 패턴

- 0x07을 AND 해서 하위 3비트를 얻는다.
  ex) 비트 번호가 17일 때, 00010001 AND 00000111 = 00000001
- 그 후 앞에서 얻은 1 만큼 1을 왼쪽으로 시프트하면 마스크를 얻는다.
  ex) 앞에서 1을 한번 얻었으므로 1비트 왼쪽 시프트 한다. => 00000010
  이 값은 17번 비트를 찾으려면 2번째 바이트에서 어디를 봐야 하는지 알려준다.

배열 인덱스와 비트 마스크를 사용하면 비트맵 기본 연산을 쉽게 수행할 수 있다.

> **비트 마스킹**

    프로그램 작성 시 연산 시간과 공간을 고려했을 때 **이진수**를 **직접 사용**하면 더 효율적이다. 이를 위해 이진수 표현을 자료구조로 쓰는 기법을 **비트 마스크**(bit mask)라고 한다. 비트 연산을 활용하여 정수의 이진 비트를 처리한다.  <br />
    - 더 빠른 수행 시간
    - 더 간결한 코드
    - 더 적은 메모리 사용량을 통한 성능 향상
    - 연관 배열을 배열로 대체. - 시간 및 공간을 절약할 수 있다.

<br />

**비트맵 기본 연산**

- `비트 설정하기(set, 1로 만들기)`
  - 비트들(index) = 비트들(index) OR 마스크
- `비트 지우기(clear, 0으로 만들기)`
  - 비트들(index) = 비트들(index) AND (NOT 마스크)
- `비트가 1인지 검사하기`
  - 비트들(index) = (비트들(index) AND 마스크) != 0
- `비트가 0인지 검사하기`
  - 비트들(index) = (비트들(index) AND 마스크) = 0

그리고 **자원**이 사용 가능하거나 사용 중인지 여부를 나타낼 때도 비트맵을 사용한다.
사용 중인 자원을 비트로 표현하면 0이 하나라도 있는 바이트를 찾기 위해 배열을 검색할 수 있다. 이는 각 비트를 하나씩 따로 검사하는 것보다 훨씬 효율적이다.

---

<참고><br />
[비트마스크 (Bitmask) 연산](https://katfun.tistory.com/entry/%EB%B9%84%ED%8A%B8%EB%A7%88%EC%8A%A4%ED%81%AC-Bitmask-%EC%97%B0%EC%82%B0-1) <br />
[비트맵 위키백과](https://ko.wikipedia.org/wiki/%EB%B9%84%ED%8A%B8%EB%A7%B5)<br />
[비트 마스크](https://coding-food-court.tistory.com/193)

# 문자열

문자열은 여러 문자로 이루어진 시퀀스를 `문자열(string)`이라고 한다.

문자열은 연산할 때 그 `길이`를 알아야 한다. 각 문자열을 위해 배열을 할당하는 것만으로 충분하지 않다. 길이가 변할 수 있는 가변 문자열 데이터에 작용하는 프로그램이 많기 때문이다.

문자열 길이를 추적하는 방법 <br />

- **첫 번째 바이트에 문자열 길이를 넣는다.**

  - 이 방법은 잘 작동하지만, 문자열 길이가 `255자`로 제한된다. (여러 애플리케이션은 255자로 불충분하다.)
  - 더 긴 문자열을 위해 바이트를 더 할당할 수 있지만, 부가 비용(길이를 저장하기 위한 바이트 수)이 수많은 문자열 길이를 넘어서는 경우가 생긴다.
  - 문자열은 바이트라서 메모리 정렬이 그때그때 다를 수 있다.

  길이를 저장하기 위해서 몇 바이트를 할당하려면 길이 정보는 반드시 올바른 메모리 정렬 경계에 있어야 한다.
  <br />

- **C는 1차원 바이트 배열을 사용한다.**

  - 문자열은 문자 배열이므로 C에서 1바이트를 나타내는 데이터 이름이 char이 되었다.
  - C 문자열은 길이를 저장하지 않는다는 점이 다르다.
  - 대신 문자 배열에 들어있는 문자열 데이터의 끝에 바이트를 하나 추가하고, 여기서 문자열의 끝을 표시하기 위해 NUL(\O)을 넣는다. (ASCII NUL 문자)
    이렇게 문자열 맨 마지막을 가리키는 글자를 `문자열 터미네이터`라고 한다.

  ![그림 7-5, C 언어의 문자열 저장 방식과 문자열 끝 표시 방식](https://cdn.discordapp.com/attachments/879215554379018243/992792746366603274/unknown.png)
  <br />
  문자열 길이보다 1바이트가 더 쓰였다. 문자열 터미네이터에 1바이트가 더 쓰인 것이다.

  - NUL은 대부분 기계에 주어진 값이 0인지 검사하는 명령어가 있어 좋은 터미네이터 문자이다.
  - 다른 문자를 터미네이터로 사용하면 널 문자인지 검사하기 위한 값을 적재해야 해서 비용이 더 든다.

    <br />

  - **장점**
    - 저장이 쉽다.
    - 문자열의 각 문자를 끝까지 출력해라 라는 일을 할 때 부가 비용이 들지 않는다.
  - **단점**
    - 문자열 길이를 알아내려면 문자열 터미네이터를 발견할 때까지 문자열을 스캔하면서 문자 수를 세야한다
    - 문자열 중간에 NUL을 넣고 싶으면 이 방법을 사용할 수 없다.

---

<참고><br />

[ null 터미네이터(\0)를 사용해 문자열의 끝을 식별하기](https://wikidocs.net/85741)<br />

# 복합 데이터 타입

### 구조체(structure)

사용자가 C언어의 기본 타입으로 새롭게 정의할 수 있는 사용자 정의 타입이다.
기본 타입만으로 나타낼 수 없는 복잡한 데이터를 표현할 수 있다.

- 멤버(member): 구조체를 구성하는 변수

```c
// 학생이라는 구조체 선언
struct student {
    int no;
    int score;
    char grade;
};

// student 타입의 변수 생성과 초기화
struct student kim = {3021, 94, 'A'};

// 값 출력
printf("%d %d %s", kim.score, kim.score, kim.grade);  // 3021 94 A 출력

```

예전에는 구조체를 배열의 편의 문법(syntactical sugar)으로 여겼지만, 오늘 날에는 구조체를 염두에 두고 작성한 프로그램이 많기 때문에 예전보다 더 근본적인 프로그래밍 언어 요소처럼 여겨진다.
<br />
`배열`이 `같은 타입의 변수 집합` 이라고 하면, `구조체`는 `다양한 타입의 변수 집합`을 하나의 타입으로 나타낸 것이다.
<br />
일시를 표현하는 구조체를 만든다고 생각해자

- 월, 일, 시, 분, 초 - 1바이트(unsigned char)
- 연도 - 2바이트(unsigned short)

이런 복잡한 데이터 타입을 프로그래밍 언어가 기본 제공하는 데이터 타입처럼 사용할 수 있다.

![그림 7-7 달력 이벤트 엔트리를 저장하기 위한 구조체](https://media.discordapp.net/attachments/879215554379018243/992792960095752322/unknown.png?width=781&height=189)
<br />

프로그래밍 언어는 멤버 순서가 바뀌면 문제가 될 수 있으므로, 프로그래머가 지정한 멤버 순서를 지키면서, 메모리 정렬도 지켜야 한다. 따라서 연도를 4번째와 5번째에 바이트에 위치시키면 경계에 걸치기 때문에 배치를 바꿔야 한다. => 패딩(pedding)을 추가한다.

![그림 7-8 일시를 표현하는 구조체의 패딩을 포함한 메모리 배치](https://cdn.discordapp.com/attachments/879215554379018243/992793096158990447/unknown.png)
<br />
패딩을 사용하는 대신 구조체 멤버 순서를 바꿔 7바이트만 사용할 수도 있다.

\*\* 이 예는 꾸며진 예이며 실제로 날짜와 시간을 이런 식으로 다루지 않는다.
UNIX의 방식을 표준적인 방법으로 사용하며, 1970년을 기준으로 몇 초가 지났는지 표현하는 32 비트를 사용한다. 현재는 64비트로 확장되었다.
<br />

### 공용체(union)

공용체는 C에서 사용할 수 있는 데이터 유형으로 구조체와 달리 메모리를 공유한다. 즉, struct의 경우 각 멤버들의 메모리 시작 주소가 다르지만, union의 경우 각 멤버들의 시작 주소가 모두 동일하다.

![struct vs union](https://cdn.discordapp.com/attachments/879215554379018243/992810506983317534/unknown.png)
<br />

- **Struct**: 구조체 멤버 중 가장 큰 변수의 크기 값을 기준으로 잡고, 기준의 자머지에 변수를 순서대로 배치하여 구조체의 전체 크기가 결정된다.

```c
struct struct_byte {
    double v; // 8byte
    int i[2]; // 4byte
    char c; // 1byte
}
```

![구조체의 메모리 할당](https://cdn.discordapp.com/attachments/879215554379018243/992813472599507035/unknown.png)
<br />

- **Union**; 공용체 멤버 변수 중 가장 큰 크기의 값을 하나 할당하고, 모든 멤버가 그 메모리를 공유한다.

```c
union union_byte {
    double v; // 8byte
    int i[2]; // 4byte
    char c; // 1byte
}
```

![공용체의 메모리 할당](https://cdn.discordapp.com/attachments/879215554379018243/992813238490251334/unknown.png)

<br />

공용체는 하나의 메모리 공간을 여러 방식으로 접근할 수 있기 때문에 구조체와 별개로 사용된다.

공용체는 주로 통신에서 사용된다.
패킷 단위로 데이터를 보낼 때, 보내는 건 쉽지만, 받는 입장에서는 덩어리로 온 데이터를 받아서 분해하고 다시 묶어서 보내는 것이 까다롭다. 공용체를 사용하면 보낼 때는 buffer로 한번에 보내고 받을 때는 struct의 변수로 각각 받을 수 있어 편리하다.

---

<참고><br />
[구조체와 공용체 차이](https://blog.naver.com/PostView.naver?blogId=ratoa&logNo=220658695667&redirect=Dlog&widgetTypeCall=true&topReferer=https%3A%2F%2Fwww.google.com%2F&directAccess=false)<br />
[Difference between Structure and Union in C](https://www.geeksforgeeks.org/difference-structure-union-c/)<br />
[구조체의 기본](http://www.tcpschool.com/c/c_struct_intro)<br />
[C Structure - Why use structure?](https://www.javatpoint.com/structure-in-c)<br />
[ C커스텀 자료형 이해하기5\_공용체(Union Type)이란? 정의/사용하는 이유](https://bite-sized-learning.tistory.com/315)

## 단일 연결 리스트(Singly Linked List)

![](https://miro.medium.com/max/953/1*elJncKhH_P9oQglfI1aVQA.png)

모든 원소가 데이터, 링크 쌍으로 이루어져 있고, 이 링크를 통해 자신의 후속 원소와 연결되는 구조를 말한다. 여러 개의 노드들이 순차적으로 연결된 형태를 갖는 자료구조이며, 첫번째 노드를 `헤드(Head)`, 마지막 노드를 `테일(Tail)`이라고 한다. 각 노드는 데이터와 다음 노드를 가리키는 `포인터(next)`로 이루어져 있다. 가장 마지막 꼬리 노드일 경우, 포인터로 이어진 노드 대신 Null을 가리키고 있다.

<br/>

- Push

```
- 함수의 인자로 새로운 노드를 생성한다.
- Head가 없다면 만들어주고 그 다음 새로운 노드가 Tail이 된다.
- Head가 있다면 Tail에 새로운 노드를 만들어주고 연결 리스트의 Tail 정보를 수정한다.
- Length를 1 증가시킨다.
```

- Pop

```
- Tail까지 리스트를 순회한다.
- 뒤에서 두 번째 노드의 다음 속성(포인터)을 null로 지정한다.
- 뒤에서 두 번째 노드를 Tail로 지정한다.
- Length를 1 차감한다.
```

- Shift

```
- 삭제 전 Head 노드 값을 변수에 할당한다.
- Head 노드 다음의 노드를 Head로 지정한다.
- Length를 1 차감한다.
```

- Unshift

```
- 함수 인자로 받은 값으로 새로운 노드를 생성한다.
- Head가 없는 경우에 Head와 Tail로 지정한다.
- 그렇지 않다면 새로 생성된 노드가 가리키는 다음 노드를 기존 Head 노드로 지정한다.
- 새로 생성된 노드를 새 Head로 지정한다.
- Length를 1 증가시킨다.
```

- Get

```
- 찾고자 하는 인덱스 번호가 0 이하거나, 또는 리스트의 길이와 같거나 더 크다면 null을 반환한다.
- 찾고자 하는 인덱스 번호까지 리스트를 순회하고 해당 인덱스 번호의 노드를 반환한다.
```

- Insert

```
- 인덱스 번호가 0보다 작거나 연결 리스트의 전체 길이보다 크다면 false를 반환한다.
- 인덱스 번호가 전체 길이와 같다면 가장 끝에 새로운 노드를 추가한다.
- 인덱스 번호가 0이라면 가장 앞에 새로운 노드를 추가한다.(Unshift)
- 위 경우에 모두 해당되지 않는다면 get 로직을 활용해 '인덱스 - 1'번째 인덱스의 노드에 접근한다.
- 새로운 노드를 접근한 노드의 다음 노드로 지정한다.
- Length를 1 증가시킨다.
```

- Remove

```
- 인덱스 값이 '전체 길이 - 1'과 같다면 pop을 수행한다.
- 인덱스 값이 0이라면 shift를 수행한다.
- 위에 모두 해당되지 않으면 get으로 '인덱스 - 1'번째의 인덱스에 접근한다.
- 해당 노드의 다음 노드를 다다음 노드로 지정한다.
- Length를 줄인다.
```

<br></br>

### 배열과의 비교

관리해야 하는 데이터의 양이 정해져 있지 않은 경우에는 배열이 적합하지 않다. 배열은 데이터 삽입이나 삭제 등의 작업을 해야 할 때, 기존 배열을 모두 복사하고 각 요소의 인덱스 번호를 매번 새로 부여한다.
반면에 연결 리스트는 원소 개수가 불분명한 경우 배열보다 더 효과적으로 데이터를 관리할 수 있다. 배열과 다르게 반드시 정해진 순서를 지키며 정렬되어 있지 않아도 된다.

|                           Lists                           |                                                  Array                                                   |
| :-------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: |
|                    인덱스 번호가 없다.                    |                                  인덱스 번호와 함께 순서가 정해져 있다.                                  |
|     다음 노드를 가리키는 포인터로 서로 연결되어 있다.     | 요소의 삽입과 삭제에 비용이 든다. 오래 걸린다. 배열 중간에 있는 데이터가 삭제되면, 공간 낭비가 발생한다. |
| 임의로 요소 접근이 안된다. 처음부터 탐색을 진행해야 한다. |                  인덱스를 통한 빠른 접근이 가능하다. 특정 인덱스로 바로 접근할 수 있다.                  |

<br></br>

### 이중 간접 주소 지정을 사용한 코드

<div align="center">

![](https://images.velog.io/images/ne_ol/post/eb956a90-b4e8-4ae7-b3f2-5f8b0df9d978/Screen%20Shot%202022-02-15%20at%202.49.26%20AM.png)

</div>

```
1. current0을 head 주소로 설정
2. current1은 head를, head는 리스트 원소 A의 노드를 가리킴
3. 삭제할 원소가 D가 아니기 때문에 다음 동일하게 진행. current2는 current(=A)의 next값을 가리킴
4. 삭제할 노드가 나올 때까지 반복
5. D를 찾았을 때, C.next를 D.next값으로 할당
```

<br></br>

# 동적 메모리 할당

### 동적 메모리 할당이란

<br/>

프로그램이 실행 도중에 동적으로 메모리를 할당받는 것을 의미한다.  
프로그램은 필요한 만큼의 메모리를 시스템으로부터 할당받아서 사용하고, 사용이 끝나면 시스템에 메모리를 반납한다.  
필요한 만큼만 할당받고, 또 필요한 때에 사용하고 반납하기 때문에 메모리를 효율적으로 사용할 수 있다.  
ex. C언어에서는 malloc()계열의 라이브러리 함수를 사용하여 동적으로 메모리를 사용할 수 있음.

<br/>

<p align="center">
<img width="600" src="https://user-images.githubusercontent.com/80025242/178111126-3b805759-17cc-4865-8b63-9f4ec86b68cb.png" alt="동적 메모리 할당 구현 이미지"/>
</p>

<br/>

<b>_static_</b> 배열 등의 변수가 사용하는 메모리는 정적이다. 이런 변수에 할당된 주소는 변하지 않는다.  
<b>_dynamic_</b> 리스트 노드가 사용하는 메모리는 동적이다. 이들은 필요에 따라 생기기도 하고, 사라지기도 한다.  
--> 이런 동적인 대상에 사용할 메모리는 `힙(heap)`에서 얻는다.

<br/>

### MMU란

<br/>

<p align="center">
<img width="600" src="https://user-images.githubusercontent.com/80025242/178113372-8173c102-3742-4c11-9f7e-ef0900c1b51a.png" alt="MMU와 CPU의 관계"/>
</p>

<br/>

Memory Management Unit 의 약자.  
메모리 관리의 핵심적인 역할을 담당한다.  
CPU 코어 내에 탑재되어 실제 메모리와 가상 메모리 사이에서 **주소**를 변환하는 작업을 한다.

# 더 효율적인 메모리 할당

<br/>

<p align="center">
  <img width="300" src="https://user-images.githubusercontent.com/80025242/178113788-750dcebe-1db6-403c-af38-05674c943658.jpeg" alt="문자열이 들어 있는 리스트 노드"/>
</p>

<br/>

<p align="center">
  <img width="450" src="https://user-images.githubusercontent.com/80025242/178113835-95764b8d-7cf5-4bab-aae1-b200be56cfb6.jpeg" alt="더 효율적인 메모리 할당"/>
</p>

# 가비지 컬렉션

### 가비지 컬렉터란

<br/>

C나 C++같은 언어는 메모리의 할당과 해제를 직접, 지시하여 관리했다.  
아무리 신중하게 코드를 짜더라도 비워줘야하는 메모리 공간을 깜빡 놓쳐버리면 `메모리 누수(memory leak)`가 생긴다.  
그래서 자바를 비롯한 새로운 언어들에서는 **가비지 컬렉터** 를 도입하게 된다.

이렇게 메모리를 알아서 관리하는 언어를, managed language 라고 한다. 반대는 unmanaged language.  
프로그래머가 필요없는 메모리를 직접 해제해주지 않아도 가비지 컬렉터가 알아서 불필요한 메모리를 비우게 된다.

<br/>

### 가비지 컬렉터가 동작하는 방식

<br/>

- Mark and Sweep

  메모리를 처음부터 끝까지 훑으면서 필요한 것과 필요하지 않는 것을 마크하고, 마크되지 않는 것들은 해제시키는 방식.  
  --> 루트에 닿지 않는 변수와 함수들을 치운다고 생각하면 된다.

- Referencing Counting

  참조 카운팅. 한 요소가 다른 요소에게 몇 번 참조되는지 횟수를 세어서 그 수가 0이 되면 해제시키는 방식.  
  --> 순환 참조하게 두지 말것 !!

<p align="center">
  <img width="150" src="https://user-images.githubusercontent.com/80025242/178114345-ee0532e3-02c0-48e9-9794-b95666e5f68b.png" alt="순환 참조 예시"/>
</p>

<br/>

### 가비지 컬렉터를 사용하면 프로그래머는 메모리 관리에 무신경해도 될까

<br/>

답은 당연히 **Nope** 이다.  
프로그램의 특성에 따라 프로그래머가 직접 할당과 해제를 해주는 편이 더 맞을 수도 있다.  
즉, 프로그램의 특성이 좌우하는 것이지 항상 가비지 컬렉터가 옳은 것은 아니다.  
그리고 분명 가비지 컬렉터의 알고리즘이 놓지는, 해제되야하는 메모리를 찾지 못하는 경우도 있기 때문에, 이런 경우엔 프로그래머가 직접 해제해줘야한다.  
좋은 프로그래머는 메모리가 낭비되는 것을 막을 방법을 항상 염두에 두어야한다.

# 이중 연결 리스트 (doubly linked list)

노드에 다음 원소와 이전 원소의 포인터를 가지고 있는 리스트

![1231](https://s3.ap-northeast-2.amazonaws.com/opentutorials-user-file/module/1335/2949.png)

> 장점

특정 위치 인덱스 탐색 시 유리하다.  
단일 연결 리스트는 한 방향으로 밖에 탐색할 수 없지만 양방향으로 탐색이 가능하다.  
현실에서 사용하는 대부분은 이중 연결 리스트

> 단점

변수를 하나 더 저장하면서 메모리를 더 많이 사용한다.

### 참고자료

- [Doubly linked list (이중 연결 리스트)](https://opentutorials.org/module/1335/8940)

# 계층적인 데이터 구조

### 트리(tree)

**트리 구조**  
한 노드에서 시작해 다른 정점들을 순회하여 자기 자신에게 돌아오는 순환(cycle)이 없는 연결 그래프  
부모노드와 자식노드 간 1:N 관계

이중 연결 리스트 탐색 시 시간 복잡도 `O(n)`  
트리 탐색 시 시간 복잡도 `O(log n)`

**2진 트리(binary tree)**

한 노드가 최대 2개의 노드와 연결된 트리
트리에 데이터를 추가할 경우 트리를 변경할 필요가 없기 때문에 \*\* 을 만들 이유가 없다.

```
struct Node {
  int data;
  Node *left;
  Node *right;
}
```

![1](https://velog.velcdn.com/images%2Fkimdukbae%2Fpost%2Ffefd2e62-bc4f-427a-a364-2ebc0b0c5c70%2Fimage.png)

### NoSQL

RDBMS와 달리 고정된 스키마가 없는 계층형 데이터베이스  
빅데이터, 분산 환경에서 대용량의 데이터 처리를 위해 개발

ex) MongoDB, Oracle

### 참고자료

- [계층적 자료구조의 탐색](https://makemethink.tistory.com/138)

## 대용량 저장장치

### 아이노드(i-node)

<div align="center">

![](https://velog.velcdn.com/images%2Fredgem92%2Fpost%2Fb832b64d-d3d9-4ceb-b08f-dcf286a4c0db%2Fimage.png)

</div>

디스크 블록에 대한 `인덱스(index)와 노드(node)`를 합친 단어로, 전통적인 UNIX 계통(리눅스)에서 파일 시스템을 처리할 때 사용하는 자료구조이다. 파일을 빠르게 찾기 위해 리눅스의 모든 파일에 일종의 번호를 부여한 것이다. 또한, 번호 외에도 해당 파일에 대한 정보도 가지고 있다. 즉, 아이노드는 `리눅스 시스템에서 파일에 대한 정보(메타 데이터)를 가진 일종의 데이터`라고 할 수 있다.
모든 파일이나 디렉토리는 고유한 아이노드를 갖고 있고 이 아이노드 번호로 구분이 가능하다. 사용자가 파일에 액세스하기 위해 파일 이름을 사용하지만, 내부적으로는 디렉토리 테이블에 저장된 아이노드 번호로 매핑되는 것이다.

- 아이노드가 갖고 있는 메타 데이터

```
- 파일 모드(permission)
- 링크 수
- 소유자명
- 그룹명
- 파일 크기
- 파일 주소(섹터 위치)
- 마지막 접근 정보
- 마지막 수정 정보
- 아이노드 수정 정보
```

리눅스 환경이라면 아래 예시처럼 `ls -i [파일 or 디렉토리]` 명령어로 아이노드 값을 확인할 수 있다.

```Bash
$ ls -i /etc/sysctl.conf
140625 /etc/sysctl.conf

$ ls -i /etc/sysctl.d/
140859 10-console-messages.conf  140862 10-link-restrictions.conf  140865 10-ptrace.conf         140868 99-sysctl.conf
140860 10-ipv6-privacy.conf      140863 10-magic-sysrq.conf        140866 10-zeropage.conf       140869 README.sysctl
140861 10-kernel-hardening.conf  140864 10-network-security.conf   140867 99-cloudimg-ipv6.conf
```

<br></br>

### 아이노드의 특징과 구조

<div align="center">

![](https://velog.velcdn.com/images%2Fredgem92%2Fpost%2Fd9bcaff6-2ffc-4404-a40e-a892f490b769%2Fimage.png)

</div>

아이노드는 한 파일이 사용하는 모든 블록을 가리키는 `포인터`들을 포함하는 하나의 블록이다. 각각 담당하고 있는 파일이 있는데, 그 파일이 사용하는 모든 블록을 가리킨다. 여기서 블록은 `데이터를 저장하는 단위`이다.

하나의 파일이 여러 데이터 블록(data blocks)을 가질 수 있다. 이 아이노드는 그 모든 블록의 주소를 가리키는 포인터들에 대한 정보를 포함한다. 아이노드는 이 data block들을 연결한다.

아이노드는 포인터 구조를 통해서 파일의 실제 데이터가 저장된 블록의 정보를 포함해 파일의 메타 데이터 정보만 저장한다.

아이노드에는 15개의 `Block pointer(블록 포인터)`가 있다. Block pointer는 블록의 주소를 가리키는데, 이 블록은 하나의 데이터 모음 덩어리를 말한다. 보통 표준 4KB 데이터 블록을 사용하며, Block Pointer는 그 블록의 주소를 담고 있다.

포인터의 종류는 총 4가지이다. `직접 블록 포인터(direct block pointer)`, `간접 블록 포인터(indirect block pointer)`, `2중 간접 블록 포인터(double indirect pointer)`, `3중 간접 블록 포인터(triple indirect pointer)`가 있다. 파일의 용량이 클수록 데이터 정보를 담는 직접 블록의 크기를 늘리면 비효율적이다. 따라서 이를 나머지로 소개된 포인터들로 처리한다. 위에 언급한대로 각 간접 블록은 안에서 데이터를 직접 처리하는게 아니라 특정 블록을 접근할 수 있게 주소를 담고 있는 것이다.

단일 간접 블록의 경우 4KB / 4byte = 1024개의 데이터 주소를 담는다. 그리고 2중 간접 블록은 단일 간접 블록의 주소 1024개를 담고 있다. 계산하면 1024 x 1024 x 4KB = 4GB정도의 데이터에 접근할 수 있다. 3중 간접 블록은 2중 간접 블록의 주소 1024개 담고 있다. 이런 구조를 통해 파일은 비교적 적은 블록을 가지고 있어도 대량의 데이터를 관리할 수 있다.

<br></br>

### 링크

> 심볼릭 링크

<div align="center">

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fc1MOld%2Fbtq27oZFH8n%2FUkKBhyI7vfSEY8Rf8OMD5K%2Fimg.png)

</div>

윈도우 시스템에서 제공하는 바로가기 기능과 유사하다. 원본 파일에 대한 정보가 포함되어 있지 않으며 원본 파일 위치에 대한 포인터만 포함되므로 새로운 아이노드를 가진 링크파일이 생성된다.

`ln –s [원본 파일] [링크 파일]`

<br/>

> 하드 링크

<div align="center">

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fchc39W%2Fbtq3dw9wAuO%2F6DGSeBHLxeyk6KdyHYeedK%2Fimg.png)

</div>

하드 링크는 디렉토리 구조에 대한 항목만 파일로 생성되지만 원본 파일의 아이노드 위치를 가리킨다. 하드 링크에는 새로운 아이노드 생성이 없다. 파일 시스템에 있는 데이터를 복사한 것이 아니라 아이노드 번호만 복사했기 때문에 일반적인 복사본과는 다르게 파일 시스템 내의 데이터 자체가 그대로 1개만 존재한다.

`ln [원본 파일] [링크 파일]`

<br/>

> 비교

가장 큰 차이는 새로운 아이노드 생성 여부이다. 이 차이에 따라 원본 파일이 삭제할 경우 접근 가능 여부도 달라진다.

|      구분      |          하드 링크          |      심볼릭 링크      |
| :------------: | :-------------------------: | :-------------------: |
|     명령어     |             ln              |         ln -s         |
|   접근 방식    | 원본과 같은 아이노드 테이블 |  원본과 다른 테이블   |
|  디스크 공간   |          필요 없음          |   약간의 공간 필요    |
|    디렉토리    |           불가능            |         가능          |
|  파일 시스템   |  동일한 파일 시스템만 가능  | 다른 파일 시스템 가능 |
| 원본 파일 제거 |          이상 없음          |      접근 불가능      |

<br></br>

### 참고자료

- [[운영체제] 파일 시스템, inode 방식에 대하여](https://velog.io/@redgem92/%EC%9A%B4%EC%98%81%EC%B2%B4%EC%A0%9C-%ED%8C%8C%EC%9D%BC-%EC%8B%9C%EC%8A%A4%ED%85%9C-inode-%EB%B0%A9%EC%8B%9D%EC%97%90-%EB%8C%80%ED%95%98%EC%97%AC)
- [[Linux / CentOS 7] 아이노드 (i-node) / 하드 링크, 심볼릭 링크](https://imjeongwoo.tistory.com/69)
- [리눅스 시스템의 아이노드(inode), 심볼릭 링크(Symbolic Link), 하드 링크(Hard Link)
  ](https://koromoon.blogspot.com/2018/05/inode-symbolic-link-hard-link.html)

## 데이터베이스

`데이터베이스(Database)`는 정해진 방식으로 조직화된 데이터 모음이며, `데이터베이스 관리 시스템(DBMS)`은 데이터베이스에 정보를 저장하고 읽어올 수 있게 해주는 프로그램이다. DBMS는 맨 아래의 데이터 저장 메커니즘을 감싼 여러 계층의 인터페이스로 구성된다.

<br></br>

### B Tree

<div align="center">

![](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F227D9C4459607D8013)

</div>

B-Tree는 탐색 성능을 높이기 위해 균형 있게 높이를 유지하는 Balanced Tree의 일종이다. `모든 leaf node가 같은 level로 유지`되도록 자동으로 밸런스를 맞춰준다. `자식 node의 개수가 2개 이상`이며, node 내의 `key가 1개 이상`일 수 있다.
node의 자식 수 중 최댓값을 K라고 하면, 해당 B-Tree를 K차 B-Tree라고도 한다.
정렬된 순서를 보장하고, 멀티레벨 인덱싱을 통한 빠른 검색을 할 수 있기 때문에 DB에서 사용하는 자료구조 중 한 종류이다.

이처럼 B 트리의 내부노드는 균형이 잡혀 있고, 이로 인해 검색 시간을 미리 예측할 수 있다. 또한, 공간은 차지하되 사용하지 않는 자식 링크가 있다. 만약 사용할 수 있는 자식 링크가 없으면 각 노드가 담당하는 범위를 조정하면서 쉽게 트리의 균형을 다시 잡을 수 있다.

<br/>

> B 트리의 조건

```
1. node의 key의 수가 k개라면, 자식 node의 수는 k+1개이다. 
2. node의 key는 반드시 정렬된 상태여야 한다. 
3. 자식 node들의 key는 현재 node의 key를 기준으로 크기 순으로 나뉘게 된다. 
4. root node는 항상 2개 이상의 자식 node를 갖는다. (root node가 leaf node인 경우 제외) 
5. M차 트리일 때, root node와 leaf node를 제외한 모든 node는 최소 ⌈M/2⌉, 최대 M개의 서브 트리를 갖는다. 
6. 모든 leaf node들은 같은 level에 있어야 한다. 
```

<br/>

Balanced tree를 사용하는 이유는 뭘까? 일반적인 트리인 경우 탐색하는데 평균적인 시간 복잡도로 O(logN)을 갖지만, 트리가 편향된 경우 최악의 시간복잡도로 O(N)을 갖게 된다.

<div align="center">

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcDrnTG%2FbtrdwTnzfT0%2F3KrkRKv4NyCUiTqQtkndj0%2Fimg.png)

</div>

root node부터 탐색을 한다고 가정하고, 왼쪽처럼 편향된 트리에서 leaf node까지 탐색한다면 모든 node를 방문하기 때문에 O(N)의 시간이 걸리게 된다. 이러한 단점을 보완하기 위해 트리가 편향되지 않도록 항상 밸런스를 유지하는 트리가 필요하다. 자식들의 밸런스를 잘 유지하면 최악의 경우에도 O(logN)의 시간이 보장된다.

<br></br>

### 참고자료

- [[DB/자료구조] B-Tree(B트리), B+ 트리](https://potatoggg.tistory.com/174)
- [[DB] 10. B-Tree (B-트리)](https://rebro.kr/169)
- [[자료구조] B-트리(B-Tree)란? B트리 그림으로 쉽게 이해하기, B트리 탐색, 삽입, 삭제 과정](https://code-lab1.tistory.com/217)

# 인덱스

### 인덱스란?

데이터베이스 테이블에 대한 검색 속도를 높혀주는 자료구조 (책의 목차,색인과 같은 역할)  
특정 컬럼에 인덱스 생성 시 별도의 테이블에 해당 컬럼의 값과 주소를 키,값으로 별도의 공간에 저장

![12](https://mblogthumb-phinf.pstatic.net/MjAyMDA3MTBfMzcg/MDAxNTk0MzQ0Njg4ODk4.EcvTJFgLWcrU_5vbKg_08mu2nz-2KCrKRgylEfQx-b8g.jjfRI4ky4VLUBySthfCfupNxx7Q6JwX_p8EfHHBREH8g.PNG.dnjswls23/image.png?type=w800)

### 인덱스 사용의 장점

데이터베이스 탐색 시 어느 위치에 필요한 데이터가 존재하는지 알 수 없기 때문에 Table full scan 작업이 필요했다.  
인덱스 생성 시 데이터베이스 부하 경감 및 필요 데이터를 빠르게 탐색 가능  
규모가 큰 테이블, 데이터 수정이 거의 없는 테이블, 데이터의 중복도가 낮은 컬럼에 사용 시 효율적

### 인덱스 사용의 단점

추가적인 저장공간이 필요하다.  
데이터의 변경이 이뤄지는 경우 인덱스 또한 수정이 필요하기 때문에  
데이터의 변경이 잦은 경우 인덱스에 대한 관리 소요가 많아지고  
오히려 인덱스의 성능이 저하 될 수 있다.

### 인덱스의 자료구조

> 해시 테이블(Hash Table)

`해시 테이블`: 키,값을 한 쌍의 데이터로 저장하는 자료구조  
시간복잡도가 O(1)로 검색이 매우 빠르다.  
등호 연산에 최적화 되어있어 비교가 필요한 경우 비효율적이라 실제로는 잘 사용되지 않는다.

> B+Tree

`B-Tree`의 단점으로 모든 데이터를 순회해야하는 경우 모든 노드를 방문해야해 비효율적인 문제를 개선시킨 트리  
오직 `leaf node`만 데이터를 가지고 나머지 노드에서는 자식 노드의 포인터만 저장한다.  
leaf node끼리는 linked list 로 연결되어 있다.  
=> 모든 데이터 순회 시 모든 노드를 방문할 필요가 없다.

![1](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbAARBC%2FbtrdDydoUp7%2F9h4KOXBRyDNKpKDAe2ugq0%2Fimg.png)

### 참고자료

- [인덱스(Index)](https://rebro.kr/167)

# 데이터 이동

프로그램은 한 지점에서 다른 지점으로 데이터를 이동시키기 위해 많은 시간을 소비한다.

- 연결리스트 대신 배열을 사용하려면 배열 크기를 증가시킬 필요가 있을 떄마다 데이터를 복사해야함
- 페이지 테이블을 MMU에 넣거나 꺼낼 때
- 디스크 비트맵을 디스크에 저장하거나 읽을 때

이를 효율적으로 하는 게 중요하다.

<br>

> ### `Loop Unrolling`
>
> 루프 언롤링은 반복문을 보다 효율적으로 풀어서 작성하는 방식으로, 바이너리 코드의 크기는 증가하지만, <u>하드웨어 가속을 추구하는 기법이다.</u> `일어나는 동기화`, `인덱스 증가`, `비교문`과 같은 불필요한 계산 시간을 줄여서 프로그램이 수행하는 시간을 줄일 수 있다.

<hr>

```js
// before
let sum = 0;
while (i < 100) {
    sum += i
    console.log(`${i}까지의 합계는 ${sum}입니다.`);
}

// after
while (i < 100) {
    sum += i
    console.log(`${i}까지의 합계는 ${sum}입니다.`);

    i++
    sum += i
    console.log(`${i}까지의 합계는 ${sum}입니다.`);

    i++
    sum += i
    console.log(`${i}까지의 합계는 ${sum}입니다.`);

    i++
    sum += i
    console.log(`${i}까지의 합계는 ${sum}입니다.`);

    i++
    ...
}
```

- (장점) Loop의 오버헤드를 줄이는 것과 캐시 히트율 상승을 도모
- (단점): 코드 사이즈가 증가하며, 가독성을 해침. 일정 배수부터는 오히려 성능이 하락할 수 있음

<br>

> ### `더프의 장치`

<hr>

루카스 필름에서 일하던 톰 더프(Thomas Duff)가 개발한 루프 언롤링 기법이다.

- 리얼 타임 애니메이션 프로그램의 속도를 향상시키기 위해 사용함
- 본인은 이 기법에 대해 자랑스러움과 역겨움을 동시에 느낀다고 한다..

**<주의> 오늘날의 컴파일러는 이 정도의 최적화는 알아서 해 주므로 굳이 더프의 장치처럼 코딩할 필요는 없다고 한다.**

```js
// 더프의 장치는 C언어로 구현되어 자바스크립트랑 정확히 대칭되는 예시가 없어
// 밑의 예시가 정확한 예시는 아니지만 루프 언롤링 기법을 사용했다고만 참고하면 될 것 같습니다.

// before
for(int i = 0; i < 100; i++) {
    myArray[i] += 1;
}


// after
for(int i = 0; i < 100; i+10) {
    myArray[i] += 1;
    myArray[i+1] += 1;
    myArray[i+2] += 1;
    myArray[i+3] += 1;
    myArray[i+4] += 1;
    myArray[i+5] += 1;
    myArray[i+6] += 1;
    myArray[i+7] += 1;
    myArray[i+8] += 1;
    myArray[i+9] += 1;
}
```

<br>

> ### 참고

- [Loop_unrolling (루프 풀기)](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=acwboy&logNo=50083036889)
- [Loop unrolling](http://emal.iptime.org/noriwiki/index.php/Loop_unrolling)
- [더프의 장치 (Duff's device)](https://johngrib.github.io/wiki/duff-s-device/)

# 벡터를 사용한 I/O

`vectored I/O` `scatter/gather I/O`  
단일 프로시저의 호출로 여러 벡터로 된 버퍼의 데이터를 읽어(read) 단일 데이터 스트림에 데이터를 쓰거나(write)  
단일 데이터 스트림에서 데이터를 읽어와 여러 벡터로 된 버퍼로 데이터를 쓰는 입출력 방식

`분산(gathering)/수집(scattering)`  
버퍼들에서 데이터를 수집하거나 분산하는 프로세스

하나의 오디오 파일을 오디오 장치로 복사하는 경우 여러 프레임으로 이루어진 하나의 파일에서  
프레임의 각 요소들을 가리키는 포인터, 크기로 구성된 벡터들로 구성된 버퍼들로 복사해  
오디오 장치에서 각 벡터에 저장된 데이터를 활용해 오디오 프레임을 조합

### 참고자료

- [WIKIPEPIA - Vectored I/O](https://en.wikipedia.org/wiki/Vectored_I/O)

# 객체 지향의 함정

<br/>

### 객체 지향 언어

<br/>

종류 : 자바, C++, 파이썬, 자바스크립트  
정의 : 객체에는 함수에 해당하는 `메서드(method)`와 데이터에 해당하는 `프로퍼티(property)`가 존재한다.

<br/>

<p align="center">
  <img width="300" src="https://user-images.githubusercontent.com/80025242/178116083-744978b9-5658-43f3-98a4-249f48a621a5.jpeg" alt="객체를 표현하기 위한 C 구조체"/>
</p>

<br/>

<p align="center">
  <img width="400" src="https://user-images.githubusercontent.com/80025242/178116133-1fc3638c-d649-444d-8866-1961c0e2f7d3.jpeg" alt="메서드 구조체를 별도로 묶기"/>
</p>

<br/>

C로도 충분히 객체의 기능을 구현해낼 수 있다.  
객체가 모든 문제의 해답은 아니다. 위 그림처럼 객체와 관련된 부가 비용도 어느 정도 존재한다.  
전역적으로 정의된 함수 대신, 객체 본인이 사용할 메서드에 대한 포인터를 항상 가지고 다녀야한다.  
그래서 객체 내의 데이터가 데이터만을 저장하는 구조만으로 꽉 채워져있지 않다. (어떤게 효율적이고 적합한지는 프로그램의 특성이 결정)  
성능이 정말 중요한 프로그램은, 정적 메모리 할당 방식 **배열** 을 활용하라.

# 정렬

<br/>

### 정렬을 사용하는 본질적 이유

<br/>

정렬 알고리즘은 따로 충분히 공부할 수 있음.  
이 챕터에서는 정렬이 왜 필요하고 어떻게 사용해야하는지 좀 더 근본적인 이유를 톺아볼 것.

<br/>

```
정렬 대상이 포인터의 크기보다 크다면, 데이터를 직접 정렬하는 대신 데이터를 가리키는 포인터를 재배열하는 방식으로 정렬해야한다.
왜 ? 메모리를 훨씬 덜 사용할 수 있기 때문이다.
```

<br/>

### 정렬 알고리즘의 내부 동작 원리

<br/>

<p align="center">
  <img width="600" src="https://user-images.githubusercontent.com/80025242/178169061-6f70edac-2060-40f4-ab80-514029c2157c.png" alt="정렬 알고리즘 내부 동작"/>
</p>

<br/>

# 해시

메모리에 데이터를 저장하고 읽는 연산 방법에 대해 이야기한다.

임의의 길이를 갖는 임의의 데이터를 고정된 길이의 데이터로 매핑하는 단방향 함수이다. 아무리 큰 숫자를 넣어도 정해진 크기의 숫자가 나오는 함수이다.
이런 해시 함수를 적용해 나온 고정된 길이의 결과값을 해시값이라고 하며, 해시코드, 해시섬(sum), 체크섬 등으로 불린다.
<br />

### 해시 테이블, 버킷

해시테이블은 해시 함수를 이용하여 키를 해시 값으로 매핑하고, 이 해시값을 인덱스 혹은 주소로 삼아 데이터를 key와 함께 저장하는 자료구조이다.

<br />

![hashfunction](https://cdn.discordapp.com/attachments/879215554379018243/995340185007030342/unknown.png)

<br /> 단순하게 key-value로 이루어진 자료구조라고 생각하면 된다.
<br />

- **key**

  - 고유한 값으로 해시 함수의 input이다.
  - key값을 그대로 인덱스로 사요하면 key의 길이만큼 정보를 저장해야만 공간도 따로 마련해야 하기 때문에 고정된 길이의 해시로 변경한다.

- **hash function**

  - key를 고정된 길이의 hash로 변경해준다.

- **value**

  - 저장소(버킷, 슬롯)에 최종적으로 저장되는 값으로 hash와 매칭되어 저장된다.

- **bucket**
  - 데이터가 저장되는 곳이다.

<br />

**장점**

- 해시 테이블은 key-value가 1:1로 매핑되어 있어 삽입, 삭제, 검색의 과정에서 평균 O(1)의 시간 복잡도를 가진다.

**단점**

- `해시값의 범위`가 너무 크면 데이터를 너무 많이 사용하거나, 데이터가 여기저기 흩어져 메모리 접근 성능이 떨어진다.
- `해시 충돌`이 발생한다.
- 데이터가 저장되기 전 저장 공간을 미리 만들어야 하고, 공간을 미리 만들었지만 공간이 채워지지 않은 경우가 발생한다.
- hash function `의존도`가 높고, 해시 함수가 복잡하면 해시값을 만들어내는데 오래 걸린다. 해시함수는 계산하기 쉬워야 하고, 키를 골고루 버킷에 뿌려주어야한다.
  <br />

### 해시 함수의 충돌

서로 다른 key가 hashing 후 같은 hash값이 나오는 경우가 있는데 이를 해시 충돌이라고 한다. 해시 충돌 발생 확률이 적을수록 좋은 해시 함수이다. 해시 충돌이 균등하게 발생하도록 하는 것도 중요하며, 모든 키가 같은 해시 값이 나오게되면 데이터 저장 시 비효율성도 커지고, 보안이 취약해져 좋지 않다.
해시 함수 충돌을 해결하기 위해 해시 체인을 사용하기도 한다.
<br />

### 해시 체인

![hash chaining](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FnMfgg%2FbtqS1WyRuWI%2F32LmJGOvrT9YTndHMvYW50%2Fimg.png)

체이닝은 저장소(버킷)에서 충돌이 발생하면 기존 값과 새로운 값을 연결리스트로 연결하는 방법이다.

- **장점**
  - 미리 충돌을 대비해서 공간을 많이 잡아놓을 필요가 없다. 출돌이 나면 그때 공간을 만들어서 연결만 해주면 된다.
- **단점**

  - 같은 hash에 자료들이 많이 연결되면 검색시 효율이 낮아진다.
  - 이를 해결하기 위해 Open Addressing(개방주소법)은 충돌이 일어나면 비어있는 hash에 데이터를 저장하는 방법이 있다. 개방주소법의 해시 테이블은 hash와 value가 1:1관계를 유지한다.
    <br />

    > 위의 그림에서 John과 Sandra의 hash가 동일해 충돌이 일어난다. 이때 Sandra는 바로 그 다음 비어있던 153 hash에 값을 저장한다. 그 다음 Ted가 테이블에 저장을 하려 했으나 본인의 hash에 이미 Sandra로 채워져 있어 Ted도 Sandra처럼 바로 다음 비어있던 154 hash에 값을 저장한다.

    이렇게 비어있는 해시 값을 찾는 방법에는 `선형 탐색`, `제곱 탐색` 등 여러 방법이 있다.

### 해시함수의 종류

**division method**

- 가장 기본적인 해시 함수.
- `숫자로 된 키 값 / 해시테이블 크기 m` 값을 해시값으로 변환한다. 간단하면서도 빠른 연산이 가능하다.
- 해시의 중복 방지를 위해 테이블의 크기 m은 소수로 사용하는것이 좋다. 하지만 남는 공간이 발생해 메모리상으로 비효율적이다.

**multiplication method**

- 숫자 키 k, A는 `0<A<1` 사이의 실수 일때 `h(k) = (ka mod 1)\*m` 으로 계산한다.
- 2진수 연산에 최적화된 컴퓨터구조를 고려한 해시함수이다.

**univeral hasing**

- 여러 개의 해시함수를 만들고, 이 `해시함수의 집합`에서 무작위로 해시함수를 선택해 해시값을 만드는 기법.
- 서로 다른 해시함수가 서로 다른 해시값을 만들어내기 때문에 같은 공간에 매핑할 확률을 줄이는 것이 목적이다.

---

<참고>
<br />
[[자료구조]해싱, 해시 테이블 그리고 Java HashMap](https://velog.io/@adam2/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0%ED%95%B4%EC%8B%9C-%ED%85%8C%EC%9D%B4%EB%B8%94)<br />
[해시](https://namu.wiki/w/%ED%95%B4%EC%8B%9C)

# 효율성과 성능

요즘은 `덜 효율적인 알고리즘`을 돌려도 `더 많은 프로세서`를 사용하면 `더 효율적인 알고리즘`을 `더 적은 프로세서`에서 실행할 때보다 더 나은 성능을 얻을 수 있다.
<br />

### 데이터베이스 샤딩 (수평 파티셔닝)

데이터베이스를 각각 다른 기계에서 실행되는 여러 `샤드`로 나누는 방식.
하나의 거대한 데이터베이스 테이블을 `수평 분할`하여 여러 작은 단위로 나눈 후, 물리적으로 다른 위치에 분산해 저장,관리하는 기술이다.
<br />
**장점**

- 각각 자체 cpu, 메모리, 디스크가 있는 독립 서버에서 확장성을 위한 방법을 제공한다.
  - 부하를 분산시키고, 더 많은 트래픽과 처리를 위해 더 많은 시스템을 추가한다.
  - 데이터베이스의 `크기`와 시스템 `리소스`의 `적절한 균형`을 유지할 수 있어 애플리케이션 `성능` 및 `확장성`이 향상된다.
- 작업을 병렬적으로 수행할 수 있기 때문에 성능이 향상된다.
  - 단일 데이터베이스에서 쿼리를 하면, 결과를 찾기 위해 모든 행을 검색해야 할 수도 있다. 이 경우 쿼리가 엄청 느려질 수도 있다. 그러나 한 테이블을 여러 개의 테이블로 분할하면 쿼리 행 수가 줄어들고, 결과 집합이 더 빠르게 반환된다.
- `애플리케이션의 안정성`을 높인다.
  - 샤딩을 사용하지 않으면 전체 데이터베이스가 손상된 경우 전체 애플리케이션을 사용할 수 없는 경우가 있는데, 샤딩을 사용하면 일부 데이터베이스가 손상되더라도, 전체가 손상된 것보다 영향이 덜하다.

<br />

- **단일 샤드** : 각 데이터베이스 작업은 단일 고객 트랜잭션과 같은 단일 샤드에 대해 수행된다.
- **다중 샤드** : 이는 일반적으로 하나 이상의 샤드에 대해 병렬로 수행되는 분석 쿼리에 적용되므로 인상적인 성능 결과를 얻을 수 있다.
  <br />

### 맵리듀스(MapReduce)

구글에서 대용량 데이터 처리를 분산 병렬 컴퓨팅에서 처리하기 위한 목적으로 제작해 발표한 소프트웨어 프레임워크이다.

맵과 리듀스 총 두 단계로 구성되며 `맵` 함수는 데이터를 입력받아 쪼개고, `리듀스`에서 원하는 결과를 얻어내는 것이라고 볼 수 있다.<br />
![맵리듀스](https://t1.daumcdn.net/cfile/tistory/99FC4B345B62DEB71C)
<br />

**장점**

- 단순하고 사용이 편리하다
- 유연하고, 특정 데이터 모델이나 스키마 정의, 질의 언어에 의존적이지 않아 비정형을 데이터 모델을 유연하게 지원 가능하다.
- 저장 구조와 독립적이다.
- 확장성이 높다.

**단점**

- 복잡한 연산이 어렵다.
- 기존 DBMS가 제공하는 스키마, 질의 언어, 인덱스 등의 기능을 지원하지 않는다.
- 상대적으로 성능이 낮다. 예를 들면, 모든 Map과정이 진행될 때 까지 Reduce는 시작될 수 없다. 즉, 맵리듀스는 병렬화를 수행할 수 없으므로 성능이 낮아질 수 밖에 없다.

---

<참고>
<br />
[맵리듀스 개념 정리](https://songsunbi.tistory.com/5)<br />
[[하둡] 맵리듀스(MapReduce) 이해하기](https://12bme.tistory.com/154)<br />
[데이터베이스 샤딩](http://wiki.hash.kr/index.php/%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4_%EC%83%A4%EB%94%A9)
