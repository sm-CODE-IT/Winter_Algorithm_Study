### 학습 정리한 내용
# Java 언어를 이용하여 정렬할 때 시간초과 문제

## 시간초과가 주로 발생하는 부분

### Java의 입력: Scanner 대신 BufferedReader 사용

#자바 **표준 입출력 라이브러리** 사용법 정리 *→ Scanner보다 시간 단축 !!*

BufferedReader는 데이터를 사용자가 요청할 때마다 매번 읽어오는 것이 아닌, 버퍼에 일정량만큼 보관해두었다가 한 번에 읽는다. 따라서 속도가 향상하고 시간 부하를 줄일 수 있다. 

| Scanner | BufferedReader |
| --- | --- |
| space를 모두 경계로 인식 | enter(’\n’)만을 경계로 인식 |
| 가공이 쉬움 | 다량의 데이터를 입력받는 경우 효율이 좋음 |
| - 효율성이 낮음
- 시간이 오래 걸림 | - Scanner와 달리 Exception 처리가 자체적으로 되어 있지 않아 따로 처리가 필요함
- 한 줄 안에서 공백을 기준으로 나눠야 한다면 StringTokenizer 를 따로 사용해야 함 |

**사용 방법**

1. main 클래스에 "throws IOException" 추가

2. 입력값 셋팅

3. 변수에 입력 값 저장하기

[줄 기준 입력]

```java
BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); -> 라이브러리 가져오기
```

[공백 기준 입력]

```java
StringTokenizer st = new StringTokenizer(br.readLine());
String[] line = br.readline().split(" ");
int[] arr = new int[line.length];

for (int i=0; i<line.length; i++) {
		arr[i] = Integer.parseInt(line[i]);  // 정수형일 때
}

while((tmp = br.readLine()) != NULL){    // 전체 입력 저장할 때
		str += tmp + "\n";
}
```

- BufferedReader, StringTokenizer은 기본적으로 String으로 읽음 => 다른 자료형에 대해서는 형 변환 필요
- parseInt, parseDouble, parseFloat 등  int, double, float형 가져오기
- 공백 기준으로 입력 받다가 줄 바꿈하려면?
    
    `st = new StringTokenizer(br.readLine(), " ");`
    

### Java의 출력: System.out.println() 대신 StringBuilder / BufferedWriter 사용

System.out.println() 의 내부

```java
public void println(String x) {
     synchronized (this) {
         print(x);   // 출력
         newLine();  // 새로운 줄 생성
     }
}
```

synchronized block 으로 씌워져 있어 동기화가 이루어진다. 동기화는 하나의 프로세스마다 존재하는 하나 이상의 쓰레드에서 공유 데이터가 존재하는 경우, 작업 중인 쓰레드가 하나라도 있으면 다른 쓰레드의 접근을 막는다. 이때 동기화는 접근을 막음으로써 쓰레드들의 대기시간이 발생하게 되는데 이는 오버헤드를 불러오게 된다. 

즉, System.out.println 에는 동기화가 적용되어 호출만으로 오버헤드가 따르게 된다. 

이러한 이유로 프로젝트 개발 시 로그를 sout 으로 남기는 것을 비권장한다.

<aside>
❗ ***오버헤드(overhead)**란 ?*

어떤 처리를 하기 위해 들어가는 간접적인 처리 시간, 메모리 등

예시

- A라는 처리를 단순하게 실행한다면 10초 걸리는데, 안전성을 고려하고 부가적인 B라는 처리를 추가한 결과 처리시간이 15초 걸렸다면, 오버헤드는 5초가 된다.
- B를 개선해 B'라는 처리를 한 결과, 처리시간이 12초가 되었다면, 이 경우 오버헤드가 3초 단축되었다고 말한다.
</aside>

**StringBuilder 클래스를 사용하면?**

```java
StringBuilder sb = new StringBuilder();
sb.append("출력할내용\n");
sb.append("출력할내용").append("\n");   // 위 코드보다 개행을 나누어서 append 하는 것이 시간적으로 더 빠르다
```

[StringBuilder (Java Platform SE 7 )](https://docs.oracle.com/javase/7/docs/api/java/lang/StringBuilder.html)

StringBuilder 클래스 공식 문서

**BufferedWriter 클래스를 사용하면?**

| write() | 출력할 내용을 버퍼에 담는다 |
| --- | --- |
| flush() | 버퍼를 비워내는 동시에 콘솔에 출력한다 |
| close() | 출력이 모두 끝나면, 스트림을 닫는다 |

```java
BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));  // IOException 예외처리 필요
bw.write("Hello World");
bw.flush();
bw.close();
```

### 참고 자료

[https://mygumi.tistory.com/83](https://mygumi.tistory.com/83)

[https://zzinise.tistory.com/71](https://zzinise.tistory.com/71)

[https://steady-coding.tistory.com/184](https://steady-coding.tistory.com/184)

# List와 ArrayList의 차이
<aside>
💬 **List : 인터페이스 / ArrayList : 클래스**

</aside>

List 인터페이스 안에 ArrayList, LinkedList 등이 포함되며, 공통되는 메서드를 추출해놓고 실제 구현은 클래스 내에서 이루어진다. 결국 ArrayList는 List에 상속된 클래스의 관계를 가진다.

리스트는 배열의 단점을 개선하여 크기가 동적으로 변하며, 필요한 메모리의 크기를 정확히 알 수 없는 경우에 사용한다. 

### 사용 방법

```java
ArrayList<Object> list = new ArrayList<>();
List<Object> list = new ArrayList<>();
```

Java의 제너릭(Generic) 특성에 의해 타입이 클래스의 외부에서 사용자의 필요에 따라 지정될 수 있다. 이를 통해 위와 같은 인스턴스의 형 변환이 가능해지고 내부 디테일과 메모리 함축 등에서 이점을 가진다. 

탐색에서 효율이 좋은 ArrayList와 삽입/삭제에서 효율이 좋은 LinkedList를 적절히 필요에 따라 바꾸어 사용할 수 있다. 이때 List로 선언하는 것이 유연성의 측면에서 훨씬 유리하다.
