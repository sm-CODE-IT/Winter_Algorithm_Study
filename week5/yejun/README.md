### 문제 풀이 정리
1822: https://velog.io/@dev_tmb/JAVA-1822%EB%B2%88-%EC%B0%A8%EC%A7%91%ED%95%A9

### 학습 정리한 내용

# 📍 counting sort(계수정렬)의 개념 및 시간복잡도
## 계수 정렬이란?

합병 정렬, 퀵 정렬 등의 기본 정렬 알고리즘과 달리 숫자를 비교하는 작업이 없이 **각 항목의 개수를 카운트하여 정렬**하는 알고리즘이다. **최댓값과 입력 배열의 원소 값 개수를 누적합으로 구성**한 배열로 정렬을 수행하며, 주어진 배열의 값 범위가 작은 경우에 빠른 속도로 정렬이 가능하다.

자료의 범위를 알고 있으며, 정렬할 값이 정수일 때 사용한다. 

## 기본 로직

### 1. 입력 배열의 최댓값을 크기로 하는 Counting Array 생성

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/115b0671-1020-4319-8ce4-54630c747c90/Untitled.png)

카운팅 배열의 모든 원소 값을 0으로 초기화

*필요에 따라 결과를 출력할 배열도 따로 생성

### 2. 입력 배열 원소 개수의 누적합

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/31ec89bd-a1d4-4fc0-8055-d11947a3f462/Untitled.png)

입력 배열을 처음부터 순회하면서 원소 값에 해당하는 배열의 인덱스의 원소값을 카운팅(+1)한다. 

### 3. 입력 배열과 누적합 배열을 이용한 정렬 수행

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d610dbed-3ba2-4ae5-944d-525f4304aba9/Untitled.png)

입력 배열의 각 원소에 대해 만들어둔 카운팅 배열을 조회하여 어느 인덱스로 접근해야 하는지 체크한 후, 조회한 원소의 개수를 1씩 감소하며 바로 앞의 인덱스로 올 수 있도록 한다.

## 시간복잡도 : O(N+K)

- K = 배열 내 최댓값
- K가 커질수록 무한대에 가까워져 성능이 떨어진다.
    
    ⇒ 입력값의 범위가 작을 때 높은 효율을 보인다. 
    

최댓값이 주어지지 않은 경우, 전체 배열을 탐색해야 하므로 O(n), Counting Array에 개수를 카운팅하는 과정에서 O(n)이 소요된다. 이후 결과 배열에 값을 입력하여 정렬된 배열을 얻는 과정에도 O(n)이 소요되어 최종적으로 O(n)의 시간복잡도를 가지며, 정렬 시간은 K에 종속된다. 

## 참고 자료

[[알고리즘 정리] 계수 정렬(Counting Sort)](https://velog.io/@luvlik207/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%A0%95%EB%A6%AC-%EA%B3%84%EC%88%98-%EC%A0%95%EB%A0%ACCounting-Sort)

[카운팅 정렬(Counting Sort, 계수 정렬) 알고리즘](https://8iggy.tistory.com/123)

# 📍 Java Collections Framework

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/226c2436-36e2-4eb8-8733-0cb93e034e37/Untitled.png)

알고리즘 문제를 풀기 위해 필연적으로 따르는 개념인 자바의 자료구조는 Collections라는 표준 라이브러리로 제공된다. Java Collections Framework의 의미를 살펴보면 일정 타입의 데이터들이 모여 쉽게 가공할 수 있도록 지원하는 자료구조의 뼈대라고 할 수 있다.

자바의 컬렉션 프레임워크에서 자료구조를 분류한 기준을 **형태에 따른 분류**로 바라보면, List, Queue, Deque는 데이터가 일렬로 연결된 형태의 선형 자료구조가 있고 이와 반대로 각 요소가 여러 개의 요소와 연결된 Graph, Tree 등의 비선형 자료구조가 있다. 이 두 가지 모두에 포함되지 않는 자료구조가 Set이다. 

# Collection 인터페이스

![점선은 구현관계, 실선은 확장관계이다. ](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/06d5918f-e3d4-4490-95fa-d37631b6e705/Untitled.png)

점선은 구현관계, 실선은 확장관계이다. 

*위 그림에서 녹색 부분이 구현된 자료구조의 형태로 존재하여 그대로 가져다 쓰면 되는 것이고, 푸른색 부분은 implements 하여 우리의 필요에 따라 직접 구현해야 한다. 

## Iterable 인터페이스

Iterable이란 ‘반복 가능한’이라는 의미를 가진다. 위 클래스들은 모두 Object[ ] 의 배열이 아닌, 내부에서 각각의 요소가 객체 형태를 띠는 배열이다. 즉, 객체의 데이터들을 모두 순회하며 출력하려면 사용자들이 각각의 데이터 순회 방법을 알거나 하나씩 get()과 같은 메소드를 통해 데이터를 꺼내와야 한다. 

이들은 모두 Java의 for-each 문법을 지원하며, 반복자로 구현되어 나오게 할 수 있다고 하여 이와 같은 이름이 붙은 것이다. 

<aside>
💡 **iterator를 사용하면 collection 요소를 순회할 수 있다!**

</aside>

## List 인터페이스

대표적인 선형 자료구조로, 순차적인 자료를 관리하는 데 사용한다. 배열의 한계를 극복하여 동적 크기 할당이 가능하며, 집합(Set)과 비교하자면 데이터의 중복이 허용된다는 특징이 있다. 

![List interface에 선언된 대표적인 메소드](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d4f0099f-51b6-48a6-b1e4-6d25dca221fc/Untitled.png)

List interface에 선언된 대표적인 메소드

### ArrayList

> 객체 배열
> 

Object[] 배열을 사용하면서 내부 구현을 통해 동적으로 관리한다. primitive 타입의 배열 형태와 가장 유사하다고 볼 수 있으며, 배열의 특성과 동일하게 임의의 접근이 가능하나 삭제, 삽입 시에 비효율적이다. 

### Vector

> 배열 - 동기화 지원
> 

⇒ 메모리 동시 접근에 대한 오류 방지, 멀티스레드 프로그래밍 가능

기본적으로 ArrayList와 거의 같으며, 동기화를 지원한다는 특징만 추가된다. 따라서 멀티 쓰레드에서는 안전하지만 단일 쓰레드에서도 동기화를 하여 ArrayList에 비해 속도가 약간 느리다.

**동기화를 지원한다는 의미는? 여러 쓰레드가 동시에 데이터에 접근하는 경우, 순차적으로 처리하도록 한다.*

▶️ Stack : 상자 쌓기. 맨 나중에 추가된 데이터를 먼저 꺼내는 방식  **[LIFO; Last In First Out]**
가장 최근에 추가된 자료(위치: top)부터 반환
* 가장 나중에 호출된 함수와 그 함수의 지역 변수가 사용하는 메모리는 Stack 자료 구조와 같은 방식으로 운영됨

cf. Queue : 선착순. 먼저 추가된 데이터부터 꺼내서 사용하는 방식  **[FIFO; Fisrt In First Out]**

### LinkedList

> 순차 자료구조
> 

각 요소가 다름 요소를 가리키는 주소 값을 가진다 ⇒ 논리적인 앞뒤 순서 有
자료 삽입, 삭제, 추가 시 주소 값만 변경하면 Ok! (삭제된 메모리는 가비지 컬렉터에 의해 수거)

데이터와 주소로 이루어진 **노드(Node)** 클래스를 만들어 서로 연결하는 방식이다. 즉, 객체끼리 연결한 형태로 배열의 단점을 보완하지만 검색 시에는 처음부터 연결된 노드를 차례로 방문해야 하므로 성능이 떨어진다. 

**ArrayList의 단점을 보완** ❓

- 자료 삽입, 삭제 시 , 나머지 자료를 이동시키고 빈 공간을 만들어 연속된 자료 구조 구현
- 처음 선언한 배열 크기 이상으로 요소 추가 시, 크기가 더 큰 배열 새로 생성하여 각 요소 복사

## Queue 인터페이스

선형 자료구조로, 주로 순서가 있는 데이터를 기반으로 선입선출(FIFO)을 위해 만들어진 인터페이스

- 단방향으로만 삽입, 삭제가 가능한 것이 Queue, 양방향으로 삽입, 삭제가 가능한 것이 Deque이다.
- Deque는 Queue를 implements하고, 각각의 구현체 클래스가 존재한다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/de3bc50a-3dcc-49e8-ae84-2e0c64a9db27/Untitled.png)

### LinkedList

*LinkedList는 List와 Deque를 모두 구현한다. 사실상 List, Deque, Queue의 세 가지 용도로 사용가능한 것이다. 

- 큐 또는 덱은 노드가 연결된 구조로 관리하고 싶다면? LinkedList
- Object[ ] 배열처럼 관리하고 싶다면? ArrayDeque를 사용하면 된다.

일반적인 큐와 덱의 성질을 지닌 자료구조를 사용하고자 한다면 LinkedList로 생성하는 것이 맞다.

```java
Queue<T> queue = new LinkedList<>();
Deque<T> deque = new LinkedList<>();
```

****T는 객체 타입을 의미하며, Wrapper Class부터 사용자 정의 클래스 타입까지 모두 가능하다. 단, primitive 타입은 불가능하다.***

### ArrayDeque

ArrayList와 같이 Object[ ] 배열로 구현된 형태를 가진다.  

### PriorityQueue

우선순위 큐는 데이터 우선순위에 기반하여 우선순위가 높은 데이터가 먼저 나오는 원리이다. 따로 정렬방식을 지정하지 않는다면, 낮은 숫자일수록 높은 우선순위를 가진다.  (→ sort() 메소드와 동일한 정렬기준)

## Set 인터페이스

입력 순서와 상관없이 데이터가 관리되고, 중복을 허용하지 않는 집합 클래스

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e37977b9-26fa-4526-bd31-6e21cec7e580/Untitled.png)

### HashSet

가장 기본적인 Set 컬렉션의 클래스로, 자료가 추가된 순서와 상관없이 출력되며 중복을 허용하지 않는다. 이는 Hash 기능과 Set 컬렉션이 합쳐진 형태이므로 삽입, 삭제, 조회의 성능이 매우 뛰어나다. 

주로 **아이디 중복 확인** 등과 같이 빠르게 데이터를 찾는 경우 등 해시에 의한 빠른 색인으로 활용될 수 있다. 

### TreeSet

이진 검색 트리를 활용하여 자료 정렬 → 프로그래머가 직접 ‘어떤 기준으로 값의 크기를 비교할 것인지’ 구현해야 함

**중복되지 않으면서 특정 규칙에 의해 정렬된 집합 형태를 쓰고 싶은 경우**에 사용

### LinkedHashSet

*Set 중에 순서를 보장하는 유일한 클래스이다. 하지만 데이터 중복이 허용되지 않는 점은 동일하다.

HashSet의 Link의 특징이 더해져 자연스럽게 순서가 보장된다. 즉, **중복은 허용하지 않으면서 순서를 보장받고 싶은 경우**에 사용한다.

---

# Map 인터페이스

하나가 아닌 쌍으로 되어 있는 자료를 관리하는 메서드

key-value 쌍    **key 값은 중복될 수 없다*

▶️ 주로 검색용 자료 구조로 쓰임

### HashMap

해시 방식으로 자료를 관리한다. key 값이 정해지면 그에 대응하는 해시 테이블의 저장 위치(헤시 테이블)가 정해지고 그 위치는 해시 함수를 통해 계산할 수 있다

### HashTable

멀티스레드를 위한 동기화 제공

## SortedMap 인터페이스

### TreeMap

key 값으로 자료를 정렬할 때
이진 검색 트리로 구현되어 있음!

## 어떤 자료구조를 선택해야 할까?

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a8d15ccf-ceb5-4e5a-a5f9-0a3168199558/Untitled.png)

## 참고 자료

[자바 [JAVA] - 자바 컬렉션 프레임워크 (Java Collections Framework)](https://st-lab.tistory.com/142)
