### 문제 풀이 정리
11866 : https://velog.io/@dev_tmb/%EB%B0%B1%EC%A4%80-11866%EB%B2%88-%EC%9A%94%EC%84%B8%ED%91%B8%EC%8A%A4-%EB%AC%B8%EC%A0%9C-0-JAVA


### 강의 수강 내용
# 제3-1장: 상속(Inheritance)
## 🔗 개념

### 상속(Inheritance)

기존의 클래스와 매우 밀접한 관계를 가지는 클래스를 새로 만들어야 하는 경우

→ IS-A 관계에 있는 새로운 클래스를 만드는 경우, **상속**을 이용한다.
ex. 노트북은 컴퓨터이다.(O)  컴퓨터는 노트북이다.(X) ⇒ 노트북 클래스가 컴퓨터 클래스를 상속받는다.

눈에 보이지 않아도 상속한 *Super Class(=Base Class, Parent Class*, 컴퓨터*)*의 멤버를 *Sub Class(=Extened Class, Child Class*, 노트북*)*이 모두 가진다.

### 생성자에 대한 기본적인 Rule

1. 생성자가 없을 경우, 자동으로 파라미터가 없는 디폴트 생성자가 만들어지고, 생성자가 하나라도 있을 경우 디폴트 생성자는 만들어지지 않는다.
2. 모든 서브 클래스의 생성자는 먼저 슈퍼 클래스의 생성자를 호출한다.
    1. super(…)를 통해 명시적으로 호출하거나,
    2. 그렇지 않을 경우, 자동으로 디폴트 생성자가 호출된다.

    <aside>
    🚨 **주의 사항**

   슈퍼 클래스에 디폴트 생성자가 없는데, **서브 클래스의 생성자에서 super(…) 호출을 안해주는 경우**

    </aside>


### 다형성(Polymorphism) ⭐🌷

슈퍼클래스 타입의 변수가 서브클래스 타입의 객체를 참조할 수 있다.

```java
Computer com = new Notebook();
```

com는 Computer 타입의 변수이면서, 실제로는 Notebook 개체를 참조하고 있다. 두 클래스에서 같은 메서드가 존재하는 상황이라면, 즉 Notebook 클래스에서 메서드 오버라이딩한 함수가 있는 경우에 참조하고 있는 Notebook 클래스의 메서드가 호출되도록 **동적 바인딩**이 이루어진다.

### 💻 CODE

*기억하면 좋은 코드!

```java
// 부모 클래스에 디폴트 생성자가 아닌 생성자를 명시한 경우
public Notebook(String manufacturer, String processor, int ramSize, int diskSize, double processorSpeed, double screenSize, double weight) {

        **super(manufacturer, processor, ramSize, diskSize, processorSpeed);**
        this.screenSize = screenSize;
        this.weight = weight;

}
```

## 📓 메모하기

- 객체지향 프로그램의 꽃은 **‘다형성’**이다.
- 메서드 오버라이딩과 상속을 적절히 사용하면, 필요에 따라 기능 구현을 다르게 하여 새로운 객체 생성 없이 참조만으로 접근이 가능한 유연한 프로그램을 만들 수 있다.



# 제3-2장: Object와 Wrapper 클래스
## 🔗 개념

### Object class

Java에서 모든 클래스의 상위 클래스는 Object 클래스이다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ce44bfba-ef4e-4c97-9439-200516fdb9f4/Untitled.png)

![Java의 모든 클래스는 Object 클래스의 멤버인 위 메서드들을 기본적으로 가지고 있다. *다만 의도대로 모든 것이 작동하지는 않을 수도 있다. ](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/608411b7-070f-4def-9013-382fb5fa73dc/Untitled.png)

Java의 모든 클래스는 Object 클래스의 멤버인 위 메서드들을 기본적으로 가지고 있다. *다만 의도대로 모든 것이 작동하지는 않을 수도 있다.

1. toString()

   toString()을 메소드 오버라이딩 하지 않은 원 상태로 호출하면, `package명.클래스명@객체의 해시코드` 의 형태를 반환한다.

2. equals()

   매개변수로 제공된 객체와 자기 자신의 동일성을 검사하므로, 같은 클래스 타입의 변수 2개를 비교하면 다른 것으로 판단된다. 이 메소드를 의도대로 사용하려면 override해야 한다.


### Wrapper class

> 기본 타입의 데이터를 하나의 객체로 포장해주는 클래스
>

Java에서 원시(primitive)  타입과 클래스(non-primitive) 타입(⇒ 객체)의 데이터는 근본적으로 다르게 처리된다. Object 타입의 배열에는 다형성의 원리에 의해 모든 종류의 객체를 저장할 수 있지만, int, double, char 등의 원시타입 데이터는 저장할 수 없다.

필요에 따라 원시 타입의 데이터를 객체로 만들어야 하는 상황이 생기는데, 이를 위해 Integer, Double, Character 등의 Wrapper Class가 존재하는 것이다.

**FOR 데이터 타입 간의 변환 기능**

- Autoboxing
- Unboxing

### 💻 CODE

*기억하면 좋은 코드!

```java
Object[] theArray = new Object[100];
theArray[0] = 10;   // 정수 10을 자바 컴파일러가 Integer 객체로 변환(autoboxing)해준다. 
int a = (Integer)theArray[0];  // Integer 객체로 저장되어 있는 Object 배열의 요소를 자바 컴파일러가 자동으로 정수로 변환(unboxing)해준다. 
```

> 인프런 권오흠 교수님의 ‘Java로 배우는 자료구조’ 강의의 학습 정리 내용입니다.
>

### 학습 정리한 내용

# 📍 Arrays.sort()와 Collections.sort()의 차이

자바 알고리즘에서 정렬을 해야할 때, sort() 메서드가 Arrays와 Collections 두 가지로 존재하는 것을 알 수 있다. 같은 정렬 기능을 하지만, 내부 정렬 방식 및 대상에서 차이가 있다. 

|  | 정렬 알고리즘 | 대상 | 타입 | 시간 복잡도 |
| --- | --- | --- | --- | --- |
| Arrays.sort() | DualPivotQuickSort | 배열 | primitive(기본형), reference(참조형) | 평균: O(nlogn) / 최악: O(n^2) |
| Collections.sort() | TimSort(삽입정렬+병합정렬) | 컬렉션(List, Set 등)  | reference(참조형) → 클래스의 객체 타입 | 평균, 최악: O(nlogn)  |

## Arrays.sort()

java.util.Arrays 의 메소드로, 정렬 기준 기본값은 오름차순이다. 
→ 숫자 > 대문자 > 소문자 > 한글 순으로 정렬된다.

```java
Arrays.sort(배열 참조변수)  // 오름차순
Arrays.sort(배열 참조변수, Collections.reverseOrder());  // 내림차순
```

## Collections.sort()

java.util.Collections 의 메소드로, sort()는 오름차순, reverse()는 내림차순 정렬을 구현할 수 있다.
→ 한글순 > 소문자 > 대문자 > 숫자 순으로 정렬된다. (*오름차순)

```java
Collections.sort(list);  // 오름차순
Collections.reverse(list);  // 내림차순
```

시간복잡도와 효율성에 따라 위 함수를 적절히 사용할 수 있다. 최악의 경우에서 시간 복잡도를 최소화하고 싶다면, primitive 타입의 배열 대신 reference 타입의 배열을 사용해 Arrays.sort()가 TimeSort를 수행할 수 있도록 유동적으로 사용할 수 있다. 

즉, 어떤 타입의 배열을 받느냐에 따라 실행되는 정렬 알고리즘이 달라지는 것이므로 시간 단축 시 이를 참고하면 좋다!

## 참고 자료

[https://codingnojam.tistory.com/38](https://codingnojam.tistory.com/38)

[https://yuja-kong.tistory.com/183](https://yuja-kong.tistory.com/183)

[https://devlog-wjdrbs96.tistory.com/68](https://devlog-wjdrbs96.tistory.com/68)


# 📍 BufferedReader/BufferedWriter, InputStreamReader/OutputStreamWriter의 차이

컴퓨터의 키보드, 파일, 네트워크 등으로 입력을 하면 컴퓨터의 메모리에 입력값들이 저장되었다가 콘솔, 파일, 네트워크 등으로 출력된다. 이때 데이터는 0과 1의 byte 단위로만 이동하며, 자바에서는 입출력을 실행하기 위해 Stream이 사용된다.

바이트 단위로는 그림, 문자 등 모든 종류의 데이터를 주고 받을 수 있고, 문자 단위로는 문자만 주고 받을 수 있다. 

> **InputStream / OutputStream** - 바이트 단위 입출력을 위한 최상위 입출력 스트림 클래스
**InputStreamReader / OutputStreamWriter** - 문자 단위 입출력을 위한 하위 스트림 클래스
**BufferedReader / BufferedWriter** - 바이트 단위 입출력을 위한 하위 스트림 클래스
**FileInputStream / FileOutputStream** - 바이트 단위 입출력을 위한 스트림 클래스
**FileReader / FileWriter** - 문자 단위 입출력을 위한 하위 스트림 클래스
> 

## INPUT

| 클래스 | 타입 | 설명 | 사용방법 | 메소드 |
| --- | --- | --- | --- | --- |
| InputStream | byte | 1byte 읽기 | InputStream in = System.in; | read() |
| InputStreamReader | char | 문자로 읽기 | InputStreamReader reader = new InputStreamReader(in); | read() |
| BufferedReader | String | 통째로 읽기 | BufferedReader br = new BufferedReader(reader); | readLine() |

read() 메소드는 아스키 코드의 int값으로 입력을 받는다. 여러 byte를 입력받기 위해서는 byte[ ] 의 배열 형태로 입력받아야 한다. 

```java
InputStream in = System.in;
int code = in.read();
char ch = (char) code;
```

InputStreamReader를 사용하면 char 등 원하는 타입의 문자 하나씩 입력받을 수 있고, 여기서 문자들이 조합된 하나의 문장으로 입력받고자 한다면 BufferedReader를 사용하면 된다. 

BufferedReader는 텍스트의 라인(’\n’)이 바뀔 때까지, 즉 엔터를 입력하기 전까지의 모든 텍스트를 한꺼번에 받는 역할을 한다. 

## OUTPUT

INPUT과 동일하며, BufferedWriter에서 자주 사용되는 메서드는 아래와 같다. 

| 메서드명 | 기능 |
| --- | --- |
| BufferedReader(Reader rd) | rd에 연결되는 문자입력 버퍼스트림 생성 |
| BufferedWriter(Writer wt) | wt에 연결되는 문자출력 버퍼스트림 생성​ |
| int read() | 스트림으로부터 한 문자를 읽어서 int 형으로 리턴 |
| int read(char[] buf) | 문자배열 buf의 크기만큼 문자를 읽어들임.  읽어들인 문자 수를 리턴 |
| int read(char[] buf, int offset, int length) | buf의 offset위치에서부터 length 길이만큼 문자를 스트림으로부터 읽어들임​ |
| String readLine() | 스트림으로부터 한 줄을 읽어 문자열로 리턴​​ |
| void mark() | 현재우치를 마킹, 차 후 reset() 을 이용하여 마킹위치부터 시작함 |
| void reset() | 마킹이 있으면 그 위치에서부터 다시시각, 그렇지 않으면 처음부터 다시시작 |
| long skip(int n) | n 개의 문자를 건너 뜀 |
| void close() | 스트림 닫음 |
| void write(int c) | int 형으로 문자 데이터를 출력문자스트림으로 출력 |
| void write(String s, int offset, int length) | 문자열 s를 offset 위치부터 length 길이만큼을 출력스트림으로 출력 |
| void write(char[] buf, int offset, int length) | 문자배열 buf의 offset 위치부터 length 길이만큼을 출력스트림으로 출력​​​ |
| void newLine() | 줄바꿈 문자열 출력 |
| void flush() | 남아있는 데이터를 모두 출력시킴. |

## 참고 자료

[[Java] 콘솔 입력 - InputStream, BufferedReader, Scanner](https://makemethink.tistory.com/170)

[[Java] BufferedReader, BufferedWriter를 활용한 빠른 입출력](https://coding-factory.tistory.com/251)

# 📍 String, StringBuilder, StringBuffer의 차이
<aside>
❕ **Java에서 문자열을 다루는 대표적인 클래스**

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0651d44e-4ac6-49a3-b78f-9a21699e85d1/Untitled.png)

- String
- StringBuilder
- StringBuffer
</aside>

## String

String 클래스는 불변의 속성을 가진다. 예를 들어, 문자열 더하기 연산을 수행했을 때 기존에 값이 들어있던 메모리 영역을 제거하고, 이어 붙인 문자열을 담은 새로운 값을 새로운 메모리 영역에 할당하여 이를 가리키도록 변경한다. 즉, 문자열 수정 시 String 인스턴스가 새로 생성된 것이다. 

불변하므로, 동기화에 대해 신경쓰지 않아도 되고(Thread-Safe), 내부 데이터를 자유롭게 공유할 수 있다. 

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ad0fbf7b-9aaf-45f8-9b90-b4cc076255a9/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9a134b28-4091-4b3c-9948-02df08b63664/Untitled.png)

- **문자열 연산이 적고 멀티쓰레드 환경일 경우**
- 변하지 않는 문자열을 읽을 때 사용하는 것이 좋다!
- 문자열 추가, 수정, 삭제 등의 연산이 빈번하게 발생될 때는 힙 메모리에 많은 임시 가비지가 생성되므로 String 클래스 사용을 지양해야 한다.

⇒ String의 단점을 해결하고자 가변성을 가진 StringBuilder, StringBuffer 클래스가 탄생하였다. append(), delete() 등의 멤버함수가 내장되어 있어, 해당 API를 통해 동일 객체 내 문자열 변경이 가능하다. (두 클래스는 동일한 API를 가지고 있다.)

## StringBuffer

동기화 키워드를 지원하여 멀티쓰레드 환경에서 안정적으로 사용이 가능하다. 따라서 쓰레드에 안전한 프로그램이 필요할 때나, 개발 중인 시스템의 일부가 쓰레드에 안전한지 모르는 경우에 사용하면 좋다. 

- **문자열 연산이 많고 멀티쓰레드 환경일 경우**

## StringBuilder

동기화를 지원하지 않아 단일쓰레드 환경에 적합하며, 성능이 가장 좋다. 이는 쓰레드에 안전한지 여부가 전혀 관계 없는 프로그램 개발 시에 사용하면 좋다. 

- **문자열 연산이 많고 단일쓰레드이거나 동기화를 고려하지 않아도 되는 경우**

*단순히 성능만으로 보면, 연산이 많은 상황에서 StringBuilder > StringBuffer >>> String 순으로 성능이 좋다. 

## 참고 자료

[https://ifuwanna.tistory.com/221](https://ifuwanna.tistory.com/221)

[https://12bme.tistory.com/42](https://12bme.tistory.com/42)


# 📍 Java에서 큰 수 다루기
# BigInteger

자바에서는 변수의 정수 표현 범위를 넘어가는 경우를 고려하여 int, long의 원시 타입 대신 사용할 수 있는 BigInteger 클래스를 제공한다. 문제가 제시될 때 보통 최악의 경우도 고려해야 하므로 무한의 정수가 들어갈 가능성이 있다면 BigInteger를 사용하는 것이 좋다. 

| 타입 | 범위 | 메모리 크기 (64bit 기준) | 기본/참조형 | 저장된 위치 |
| --- | --- | --- | --- | --- |
| int | -2,147,483,648 ~ 2,147,483,647 | 4 Byte | 기본형 | Stack |
| long | -9,223,372,036,854,775,808 ~ 9,223,372,036,854,775,807 | 8 Byte | 기본형 | Stack |
| BigInteger | 무한 (Infinity) | Minimum 70 Byte | 참조형 | Heap |

> BigInteger는 int, long, Integer, Long 과는 달리 문자열 형태로 숫자를 처리한다.
> 
- BigIntger는 표현하고자 하는 자리수에 비례하여 사용하는 메모리 크기가 늘어난다.
- BigIntger의 메모리 크기는 최소 사이즈인 70 Byte에서 “7”과 같이 한 자리 수로만 사용할 때의 메모리 크기이다.

→ 따라서, 해당 클래스를 사용하는 것만으로 최소 메모리를 잡아먹는 크기가 크므로 무한이 아닌지 조건을 생각해보고 사용해야 한다. 

## ❗ 사용법

BigInteger는 클래스 이므로, 사칙연산과 비교 등의 원시 타입에서의 숫자 연산을 모두 내부 메서드의 형태로 지원한다.

### 선언

```java
import java.math.BigInteger;

BigInteger bigNum = new BigInteger("1000");
```

### 사칙연산

| add(bigNum) | 덧셈(+) |
| --- | --- |
| subract(bigNum) | 뺄셈(-) |
| multiply(bigNum) | 곱셈(*) |
| divide(bigNum) | 나눗셈(/) |
| remainder(bigNum) | 나머지(%) |

*반드시 같은 BigInteger 간의 연산만 가능하다. 

### 형 변환

| intValue() | BigInteger → int |
| --- | --- |
| longValue() | BigInteger → long |
| floatValue() | BigInteger → float |
| doubleValue() | BigInteger → double |
| toString() | BigInteger → String |
| valueOf() | int → BigInteger |

### 2개의 수 비교

`compareTo` 사용

- 작은 수를 큰 수랑 비교  *50.comoareTo(100)* → -1
- 2개의 수가 같을 때 → 0
- 큰 수를 작은 수랑 비교 → 1
