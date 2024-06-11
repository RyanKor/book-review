# 마크업 언어

### 마크업 언어란?
텍스트와 구분 할 수 있는 `마크`를 추가 할 수 있는 시스템  
데이터를 기술 하는 정도로만 사용되어 프로그래밍 언어와는 구분된다  

### 종류
- 표현적 마크업  
문서의 형태를 표현하기 위한 마크업  
워드 프로세서 등에서 사용된다  
- 절차적 마크업  
문자를 처리할 프로그램의 명령을 기술한 마크업  
troff, LaTeX, 포스트스크립트가 있다.
- 기술적 마크업  
가장 많이 사용되는 종류로서 문서가 표현하는 내용을 기술하는데 사용된다  
HTML, Markdown

# 균일 자원 위치 지정자

### 균일 자원 위치 지정자(URL,Uniform Resource Locator)란?
정보 자원의 위치, 종류 등을 찾기위한 일련의 규칙을 따르는 텍스트 문자열

### URL의 구조
![1](https://dbscthumb-phinf.pstatic.net/1592_000_3/20130422115846610_L0GW21ECF.jpg/z1_1449_i1.jpg?type=ori_1&wm=Y)  
`통신 프로토콜` 데이터를 교환하는 데 사용하는 언어를 지정, 통신 메커니즘 ex)HTTP,HTTPS  
`서버` 서버의 종류 ex) www
`도메인 이름` 통신하고자 하는 서버/호스트  
`2단계 도메인` 서버의 이름  
`최상위 도메인` 국가 혹은 관리 조직 ex)com, org  
`디렉토리` 서버 안 해당 자원의 위치  


# HTML 문서

### HTML이란?
하이퍼 텍스트 마크업 언어(Hyper Text Markup Language)로 웹페이지 표시를 위해 개발된 마크업 언어  
꺽쇠 괄호(<,>)로 둘러싸인 태그로 되어있는 HTML 엘리먼트 형태로 작성  

### HTML의 구성요소
- **여는 태그**  
엘리먼트의 이름과 열고 닫는 꺽쇠 괄호로 구성  ex) `<p>`, `<title>`  
엘리먼트가 시작되는 부분부터 효과가 적용  
- **닫는 태그**  
엘리먼트의 이름 앞에 슬래시(/)가 포함 ex) `</p>`, `</title>`  
엘리먼트 효과가 종료  
- **내용**  
엘리먼트의 내용으로 단순 텍스트  
- **엘리먼트**  
여는 태그, 닫는 태그, 내용을 통틀어 요소(element)라고 한다.  

### 블록 레벨 요소 vs 인라인 요소
- **블록 레벨 요소**  
웹 상에 하나의 블록을 만드는 엘리먼트 ex)`<p>...</p>`  
앞 뒤 엘리먼트 사이의 새로운 줄을 만든다  
인라인 엘리먼트 내부에 만들 수 없지만 다른 블록 레벨 엘리먼트 내부에는 만들 수 있다  
- **인라인 요소**  
항상 블록 레벨 엘리먼트 내에 포함되어 있다  
단어같은 작은 부분에 대해서만 적용될 수 있다  
새로운 줄을 만들지 않는다  
ex) `<a>...</a>`,`<em>...</em>`,`<strong>...</strong>`


### 속성(attributes)
해당 엘리먼트에 실제로 표시되지는 않지만 추가적인 내용을 담고 싶을 때 사용  
속성 이름에 따라 미리 정의도니 동작이 있는 경우도 있다  
ex) `<a href='https://roadgram.net'>링크</a>`,`<input type='text'>text</input>`


# DOM: 문서 객체 모델

웹 브라우저는 문서를 `문서 객체 모델(DOM)`에 따라 처리한다.

`DOM`은 HTML, XML 문서의 프로그래밍 interface로, 프로그래밍 언어가 DOM 구조에 접근할 수 있는 방법을 제공하여 그들이 문서 구조, 스타일, 내용 등을 변경할 수 있게 돕는다

`DOM`은 프로그래밍 언어와 독립적으로 디자인되었다. 때문에 문서의 구조적인 표현은 단일 API 를 통해 이용가능하다. 이 문서에서는 자바스크립트를 주로 사용하였지만, <u>DOM의 구현은 어떠한 언어에서도 가능하다.</u>

마트료시카 인형의 등고선을 그린 것처럼 보이는 아래 그림은 코드의 엘리먼트를 보여준다.

<img width="400" alt="image" src="https://user-images.githubusercontent.com/91880235/180338436-86cede5f-5338-4e73-bdc7-54832841456e.png">

<img width="400" alt="image" src="https://user-images.githubusercontent.com/91880235/180338446-09d42d98-3d5d-477b-89c2-2e4cc68d0bff.png">

<br>

> ### 트리 관련 용어
<img width="400" alt="image" src="https://user-images.githubusercontent.com/91880235/180338661-8007f677-cc6e-4985-8e0d-0b7b0348e014.png">

<br>

> ### DOM 처리
브라우저는 DOM 파스 트리를 `깊이 우선 탐색(DFS)`로 트리를 해석한다. 

읽는 순서는 HTML이 작성된 순서와 동일하며 스택을 사용하는 또 다른 예로 볼 수 있다.

<img width="400" alt="image" src="https://user-images.githubusercontent.com/91880235/180338618-f8becf57-d830-41f5-862b-774b7d86aaa8.png">

<br>

> ### 요즈음의 DOM
- `DOM`
  - DOM Tree -> Render Tree 생성 -> Layout (reflow) -> Paint (repaint)
- `Virtual DOM`
  - Virtual DOM Render -> 변경된 부분만 원본 DOM에 반영
    
    ex) 30개의 요소가 변경됐을 경우 모든 변화를 묶어서 한 번만 실행하여 연산비용이 적음
  - 비교하는 방식을 `In-Memory`에서 담당하기에 메모리 사용량이 많음
  - 가상 DOM 사용 예시: `React`, `Vue`

    <img width="400" alt="image" src="https://user-images.githubusercontent.com/91880235/180341236-d52a3e02-59b6-4754-abc0-9d9413a2747b.png">

- `Incremental DOM`
  - 실제 DOM과 비교하는 방식을 채택하여 더 간단한 방식
  - 가상 DOM 사용 예시: `Angular`

    <img width="400" alt="image" src="https://user-images.githubusercontent.com/91880235/180341702-8442f0a4-09cd-4f9e-aecd-3d0f1f8f0e01.png">

최근에 `Svelte`라는 프레임워크에서는 가상돔을 사용하지 않으면서도 변환할 수 있는 모든 형태를 컴파일 하는 형태로 빠른 성능을 제공해주어 인기가 있음


<br>

> ### 참고
- https://developer.mozilla.org/ko/docs/Web/API/Document_Object_Model/Introduction
- [DOM은 뭐고 가상 DOM은 뭔가요? (+ Svelte와 React의 차이)](https://www.youtube.com/watch?v=1ojA5mLWts8)
- [[10분 테코톡] 🥁 지그의 Virtual DOM
](https://www.youtube.com/watch?v=PN_WmsgbQCo)
- [Incremental DOM과 Virtual DOM 비교](https://ui.toast.com/weekly-pick/ko_20210819)
- [React와 Angular의 DOM](https://steadev.tistory.com/88)
- [Svelte: 나무위키](https://namu.wiki/w/Svelte)


# CSS
`CSS(Cascading Style Sheets)`는 HTML이나 XML로 작성된 문서의 표시 방법을 기술하기 위한 스타일 시트 언어다. 

과거에는 HTML 내에 스타일도 포함하여 작성하다가 `관심사의 분리(HTML은 문서의 구조부분만 담당, CSS는 디자인 요소만 담당)`를 위해 W3C에서 발표하게 되었다.

<br>

> ### 셀렉터

<img width="400" alt="image" src="https://user-images.githubusercontent.com/91880235/180590646-89df748d-a9fe-47b9-ac2d-6f7d6295c36e.png">

<br>

> ### CSS의 단점
CSS도 여러가지 언어들의 요소를 섞어놓은 하나의 언어이다. CSS의 장점 중 하나는 작성이 쉽다는 것이지만 요소가 많아지고 이에 따라 코드가 늘어나기 시작하면 유지보수에 어려움이 많아진다. 

CSS의 선택자 개념을 잘 이용하면 이를 보완할 수 있으며, Less등의 기술은 기존 CSS에서 구현되지 않은 조건별 CSS 구성을 용이하게 할 수 있는 수단이다. CSS를 보완하기 위해 만들어진 기술로 `전처리기`, `CSS-in-JS`, `CSS Framework`등이 있다.

<br>

> ### CSS 라이브러리/프레임워크 종류(Trend)
- `Post-Processor(전처리기)`
  - CSS에 변수, 함수, 상속 등의 일반적인 프로그래밍 개념을 적용한 것
  - 컴파일러를 통해 CSS 포맷으로 변환
  - 종류
    - Sass/SCSS (사용량이 가장 많음)
    - Less
    - Stylus
    - Post CSS (만족도가 가장 높음)
- `CSS-in-JS`
  - JS 코드 안에 CSS를 삽입하여 컴포넌트 레벨로 추상화하여 작성할 수 있음 
  - 종류
    - Styled Component (사용량이 가장 높음)
    - vanila extract
    - Emotion
- `CSS Framework`
  - 종류
    - Bootstrap (사용량이 가장 많음)
    - Tailwind CSS (만족도가 가장 높음)
    - Material CSS
- `순수 CSS`
  - 2022 구글 I/O라는 개발자 컨퍼런스에서 @import, @scope, @media 등 신규 기능을 출시하였음(모든 브라우저에는 적용 X, 일부 실험 버전에만 적용 가능)


  # XML 등의 마크업 언어

<br/>

### XML 이란 ?

<br/>

```
XML ( eXtensible Markup Language ) 
```
```XML
<?xml version="1.0" encoding="UTF-8" ?>
<food>
    <name>귤</name>
    <sort>과일</sort>
    <cost>3000</cost>
</food>
```

W3C 에서 개발된 다목적 마크업 언어이다. `SGML` 의 단순화된 부분집합이기도 하다. ( `SGML` 보다 해석과 처리가 단순함. )     
특히 인터넷에 연결된 시스템끼리 데이터를 쉽게 주고 받을 수 있게, `HTML` 의 한계를 극복할 목적으로 만들어졌다.

<br/>

누구나 원하는대로 마크업 언어를 만들어서 사용할 수 있다.   
그렇기 때문에 같은 이름, 다른 뜻을 가진 엘리먼트끼리 충돌이 생길 수 있다.
```XML
<xml>
   <garden>
      <vegetable>
         <name>tomato</name> <!--name 중복-->
         <variety>Cherokee Purple</variety>
         <days-until-maturity>80</days-until-maturity>
         <name>Purple Tomato Salad</name> <!--name 중복-->
      </vegetable>
   </garden>
</xml>
```

<br/>

중복되는 엘리먼트끼리는 `namespace` 를 사용해 구분해준다.   
<xml> 엘리먼트의 xmlns 속성은 namespace 접두사와 url을 연결해준다.
```XML
<xml xmlns:vml="http://www.garden.org" xmlns:rml="http://www.recipe.org">
   <vml:garden>
      <vml:vegetable>
         <vml:name>tomato</vml:name>
         <vml:variety>Cherokee Purple</vml:variety>
         <vml:days-until-maturity>80</vml:days-until-maturity>
         <rml:name>Purple Tomato Salad</rml:name>
      </vml:vegetable>
   </vml:garden>
</xml>
```

<br/>

### SGML 이란 ?

<br/>

```
SGML ( Standard Generalized Markup Language )
```

```XML
<QUOTE TYPE="example">
   typically something like <ITALICS>this</ITALICS>
</QUOTE>
```

문서용 마크업 언어를 정의하기 위한 메타 언어이다.

# 자바스크립트

이전의 예제는 모두 정적(static)이었다. 그래서 미리 어떻게 표시될지 정해진 텍스트를 그대로 표시만 했다. 웹 브라우저가 표시된 내용을 바꾸는 방법은 새로운 url을 서버에 요청에 새 문서를 받아오는 방법 뿐이고, 이는 매우 느리고, 자원도 낭비한다.
<br />

마크 앤드리슨은 넷스케이프라는 회사를 창립했고, 대화형 웹 페이지가 필요하다는 사실을 인식하고 `자바스크립트` 언어를 소개했다. 그 후 Ecma International이라는 표준 위원회에 의해 ECMA-262로 표준화되었다. (자바스크립트를 Ecma 스크립트라고도 한다.)
<br />

자바 스크립트를 사용하면 브라우저에서 실행될 수 있는 실제 프로그램을 포함시킬 수 있다. 직접 DOm을 변경하고, 직접 웹서버와 통신할 수 있다.
<br />

![그림 9-8 자바스크립트가 포함된 웹 브라우저와 웹 서버의 상호작용](https://media.discordapp.net/attachments/879215554379018243/1000669988413264024/IMG_9903.JPG?width=1119&height=538)
<br />

자바스크립트와 서버의 상호작용은 비동기 자바스크립트와 XML, 즉 AJAX로 이루어진다.

- 비동기: 브라우저가 서버의 응답이 언제 일어날지에 대해 아무 제어를 하지 않는다.
- XML: 서버와 자바스크립트를 사이를 오가는 데이터 형식. 처음에는 XML을 사용

자바스크립트는`<script>` 엘리먼트로 HTML 문서에 포함시킬 수 있다.
<br />

```html
<script>
  window.onload = function () {
    var big = document.getElementsByTagName('big');
    big[0].style.background = 'green';
  };
</script>
```

<br />

window.onload로 브라우저가 문서를 읽어들인 다음 이 함수를 호출한다.

DOM 객체에서 `<big>` 엘리먼트를 모두 얻을 수 있다.
그리고 엘리먼트의 프로퍼티도 변경할 수 있다.

이 외에도 여러 함수로 DOM을 조작할 수 있고, 단순히 CSS 스타일을 변경하는 작업 이상의 일을 할 수 있다.

# jQuery

자바스크립트로 DOM을 조작할 수는 있지만, 문제가 있다.

1. DOM 함수 동작이 브라우저마다 다를 수 있다.
2. DOM 함수를 사용하기 불편하다. (사용친화적인 인터페이스를 제공하지 않는다. )
   <br />

jQuery는 2006년에 나온 라이브러리로 브라우저 사이의 불일치를 부드럽게 메꿔준다.
따라서 프로그래머가 브라우저 간의 차이를 다룰 필요가 없다. 그리고 더 쉬운 DOM 조작 인터페이스를 제공한다.
<br />

```html
<!-- 1. jQuery 라이브러리 import -->
<script
  type="text/javascript"
  ,
  src="https://code.jquery.com/jquery-3.2.1.min.js"
></script>

<!-- 2. 실제 코드  -->
<script>
  $(function () {
    $('big').css('background', 'green');
  });
</script>
```

<br />

1. 첫 번째 `<script>` 엘리먼트는 jQuery 라이브러리를 임포트한다.
2. 두 번째 `<script>` 엘리먼트에는 실제 코드가 담겨있다.
   - `$('big')`는 실렉터.
   - `.css('background', 'green')`는 실렉터로 선택한 원소에 대해 수행할 액션
     <br />

이렇게 jQuery를 사용하면 자바스크립트로 더 쉽게 DOM을 변경할 수 있다. 현재는 jQuery 외에도 상이한 자바스크립트 라이브러리가 많다.

## SVG(Scalable Vector Graphics)

번역하자면 `확장가능한 벡터 그래픽`이다. 2차원 벡터 그래픽을 표현하기 위한 XML 기반 마크업 언어이다. 픽셀을 이용하여 그림을 그리는 png, jpg 파일들과 다르게 벡터를 기반으로 이미지를 표현한다. 그러다보니 크기를 조절함에 따라 깨지는 것이 없고, 용량이 작기 때문에 웹에서 자주 사용하는 이미지 형식이다.

<div align="center">

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fd87MQp%2FbtqBcwQmjo7%2FHJhcwKkr3S7rN48YOctgD0%2Fimg.png)

</div>

<br/>

SVG 이미지는 마크업으로 쓰이므로 텍스트 에디터로 작성하고, 또 작성된 이미지를 수정할 수도 있다.
벡터를 기반으로 그려지므로 사이즈를 크게 해도 깨지지 않는다. `scalable`이라는 특징으로 어떤 해상도에서 사용하든 동일하다.
XML 포맷으로 파일이 작성되므로 JS나 CSS로 조작이 가능하나, 이미지가 복잡할수록 SVG만의 장점은 감소한다.

<br></br>

## HTML5

HyperText Markup Language의 약자로 월드와이드웹(World Wide Web)을 통해 제공되는 정보를 나타낼 목적으로 사용되는 마크업 언어이며 HTML의 5번째 버전을 의미한다.

HTML5가 만들어 지기 이전까지는 같은 웹 사이트라 하더라도 접속하여 사용하는 웹 브라우저의 종류 또는 버전에 따라 화면이 다르게 보이는 상황이 발생 했는데
이러한 이유로 웹표준의 필요성이 절실하게 요구되었으며, 이런 요구를 충족시키기 위한 기술로 HTML5가 등장하였다.

<br/>

### 주요 특징

1. HTML5 이전 버전까지는 웹 브라우저에 추가 설치된 플러그인의 도움 없이 동영상이나 음악을 재생할 수 없었으나 HTML5부터는 플러그인의 추가 설치 없이 동영상이나 음악을 웹 브라우저 상에서 곧바로 재생할 수 있다.
2. HTML5에서는 SVG 태그를 이용한 2차원 벡터 그래픽과 자바 스크립트 캔버스를 사용한 2차원 래스터 그래픽, CSS3와 자바스크립트 WebGL을 사용한 3차원 그래픽의 구현이 가능하다.
3. HTML5는 서버와 소켓 통신이 가능해 실시간으로 서버와 양방향 통신을 수행할 수 있다.
4. 스마트폰의 배터리 잔량을 확인하거나 GPS를 통한 위치 확인 및 장치 접근이 가능하다.
5. HTML5는 오프라인 상태에서도 작업이 가능하다.

<br/>

### 주요 특징

- `콘텐츠의 호환성` HTML5 이전 버전으로 제작한 콘텐츠도 문제없이 이용 가능해야 한다.

- `이전 브라우저와의 호환성` HTML5가 지원되지 않는 이전 버전의 브라우저에서도 이용 가능해야 한다.

- `이용 방법의 호환성` 기존에 HTML 태그 사용법을 최대한 사용가능하도록 해야 한다.

- `기능의 재사용기능의 재사용` 각각의 브라우저에서만 사용 가능한 기능들을 통합하여 공통적으로 사용할 수 있어야 한다.

- `혁신보다는 발전을 우선` HTML5는 새로운 언어를 구현하는 것이 아니므로 이미 사용 중인 HTML을 보다 더 사용하기 쉽도록 재구성하도록 한다.

<br/>

## JSON

`JavaScript Object Notation`의 축약어로 데이터를 저장하거나 전송할 때 많이 사용되는 경량의 데이터 교환 형식이다.

Javascript에서 객체를 만들 때 사용하는 표현식을 의미한다. 
JSON 표현식은 사람과 기계 모두 이해하기 쉬우며 용량이 작아서, 최근에는 JSON이 XML을 대체해서 데이터 전송 등에 많이 사용한다.
JSON은 데이터 포맷일 뿐이며 어떠한 통신 방법도, 프로그래밍 문법도 아닌 단순히 데이터를 표시하는 표현 방법일 뿐이다.

<br/>

<div align="center">

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FB1wJV%2FbtqSTImOlsB%2FzpskLu4DwKd8uqa7bgzw0k%2Fimg.png)

</div>

<br/>

JSON 형식은 자바스크립트 객체와 마찬가지로 `key/value`가 존재할 수 있으며 key 값이나 문자열은 항상 쌍따옴표를 이용하여 표기한다.
객체, 배열 등의 표기를 사용할 수 있으며, 일반 JS 객체처럼 원하는 만큼 중첩시켜 사용할 수 있다. JSON 형식으로는 null, number, string, array, object, boolean을 사용할 수 있다.

<br/>

AJAX는 단순히 데이터만이 아니라 JS 그 자체도 전달할 수 있다. JSON 데이터를 받았는데 단순 데이터가 아니라 JS를 받아 그게 실행 될 수 있다.
이러한 이유로 순수하게 데이터만 추출하기 위한 JSON 관련 라이브러리를 따로 사용하기도 한다.

<br/>

- `JSON.parse(JSON 형식의 텍스트)` JSON 형식의 텍스트를 자바스크립트 객체로 변환
- `JSON.stringify(JSON 형식(문자열)으로 변환할 값)` 자바스크립트 객체를 JSON 텍스트롤 변환

<br></br>

### XML과 JSON의 차이점

둘 다 데이터를 저장하고 전달하기 위해 고안되었다. 기계 뿐만 아니라 사람도 쉽게 읽을 수 있으며, 계층적인 데이터 구조를 가진다.

XML은 데이터 저장, 전달시 사용되는 마크업 언어이다. ML DOM(Document Object Model)을 이용하여 해당 문서에 접근후 XML 파서를 통해 파싱된다.
JSON은 데이터를 저장하고 전달하는 메타언어이다. 자바스크립트의 표준 함수인 eval()함수로 파싱된다.

XML은 스키마를 사용하여 데이터의 무결성을 검증할 수 있지만, 배열을 사용할 수 없고 데이터를 읽고 쓰는 것이 JSON에 비해 느리다.
JSON은 문자열을 전송받은 후에 해당 문자열을 바로 파싱하므로, XML보다 빠른 속도를 가지고 있다. 하지만 개발자가 문자열 데이터의 무결성을 검증해야 한다.


JSON은 HTML과 JavaScript가 연동된 빠른 응답이 필요한 웹 환경에서 많이 사용되고, XML은 스키마를 사용하여 데이터의 무결성을 검증할 필요가 있을 때 많이 사용된다.

<br></br>