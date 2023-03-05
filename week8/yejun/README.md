### 학습 정리한 내용
<br/>
<br/>

# 📍 분할정복을 이용하여 제곱을 구하는 방법
## 분할정복 알고리즘

> ********Divide and Conquer********
> 

크고 방대한 문제를 작은 문제로 분할하여 해결하는 방법으로, 대표적으로 정렬 알고리즘의 퀵 정렬과 합병 정렬, 이진 탐색, 고속 푸리에 변환(FFT) 등이 이를 이용한다. 

분할된 작은 문제는 입력 크기만 작아질 뿐, 기존의 문제와 성격이 동일하다. 또한, 분할된 문제들은 서로 독립적이므로 순환적인 성격을 가지고 최종적으로 결과를 통합하는 것이 가능하다. 

### 설계

1. Divide
    
    문제의 분할이 가능한 경우, 2개 이상의 하위 문제들로 나눈다.
    
2. Conquer
    
    하위 문제들을 재귀적으로 해결하며, 분할이 가능하다면 또 다시 Divide를 수행한다. 더 이상 나누어지지 않을 때까지 과정을 반복하며, 끝까지 분할했다면 탈출 조건을 설정하고 문제를 해결한다.
    
    *이때 문제를 제대로 Divide 했다면, Conquer은 쉽다. 따라서 **Divide를 제대로 하는 것**이 분할정복의 핵심이다. 
    
3. Combine
    
    Conquer한 문제들을 통합하여 원래 문제의 답을 얻는다.
    

## 거듭제곱 구하기

### 분할정복 이용 X

```java
// 재귀함수 이용
public static int pow(int a, int n) {
		if (n == 0) {
				return 1;
		} else {
				return a * pow(a, n-1);
		}
}

// 반복문 이용
public static int pow(int a, int n) {
		int result = 1;
		for (int i=1; i<=n; i++) {
				result *= a;
		}
		return result;
}
```

### 분할정복 이용 O

3^5 = 3x3x3x3x3로 5번 반복하듯이, n의 거듭제곱을 구하려면 O(n)의 시간복잡도를 가진다. n이 커질수록 성능이 크게 저하된다. 이를 개선하기 위하여 분할정복을 이용하면 O(logn)의 개선된 알고리즘으로 값을 구할 수 있다. 

이는 지수의 성질 중 결합법칙[(a*b)c = a(b*c)]을 이용한 수학 개념을 이용한다. 예를 들어, 5^10을 구한다고 할 때, 10을 2진수로 나타내면 1010이다. 이는 10진수로 계산하면 8+2이다. 따라서 5^10 = 5^8 * 5^2로 나눌 수 있다.

![n이 짝수인지, 홀수인지에 따라 재귀 방식으로 문제를 분할하고 해결한 값을 리턴하는 과정을 반복한다. ](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ca0bca81-2ee3-4316-b7ff-53a7bb9f41b1/Untitled.png)

n이 짝수인지, 홀수인지에 따라 재귀 방식으로 문제를 분할하고 해결한 값을 리턴하는 과정을 반복한다. 

매번 2로 나누어 더 작은 문제로 만들어서 해결하는 분할정복을 이용함으로써 구하고자 하는 값이 1이 되는 순간 리턴

```java
public static int pow(int a, int n) {
		if (n == 0) {
				return 1;
		} else if (n % 2 == 0) {
				int n = pow(a, n/2);
				return n*n;
		} else {
				int n = pow(a, (n-1)/2);
				return a*n*n;
		}
}

// → ‘/’ 연산자가 짝수와 홀수에서 동일한 결과(int형 선언)를 반환하므로 아래의 코드로 간결하게 나타낼 수 있다.
public static int pow(int a, int n) {
		if (n == 0) {
				return 1;
		}

		int tmp = pow(a, n/2);
		int result = tmp*tmp;
		
		if (n % 2 == 0) {
				return result;
		} else {
				return result * a;
		}
}
```

관련 백준 문제 - 11444, 18291, 1629

## 참고 자료

[https://mygumi.tistory.com/319](https://mygumi.tistory.com/319)

[https://loosie.tistory.com/237](https://loosie.tistory.com/237)

# 📍 이진수의 원리를 이용하여 제곱을 구하는 방법

## 이진수 사용 원리

0001 * 0001 = 0010

0010 * 0010 = 0100

0100 * 0100 = 1000

이진수는 위와 같이 수를 제곱하면 왼쪽으로 한 칸씩 이동하는 성질이 있다. 이를 이용하여 생긴 것이 바로 비트 연산이다. 

A^15를 구한다고 할 때, 15는 이진수로 01111이다. 이를 2로 나누다보면 01111/2=0111…1 → 0111/2=011…1 → 011/2=01…1 → 01/2=0…1로, 나머지를 조합하면 기존 이진수를 얻음을 알 수 있다. 

```java
public static int pow(a, b) {
		int n = 1;
		while (b != 0) {
				if (b % 2 == 1) {
						n *= a;
				}
				a = a*a;   // 이진수 제곱 연산
				b /= 2;    // 지수를 2로 나누어 나머지를 구한다. 
		}
		return n;
}
```

## 참고 자료

[https://velog.io/@apro_xo/Algorithm-거듭제곱을-이진수를-이용하여-해결하기](https://velog.io/@apro_xo/Algorithm-%EA%B1%B0%EB%93%AD%EC%A0%9C%EA%B3%B1%EC%9D%84-%EC%9D%B4%EC%A7%84%EC%88%98%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%98%EC%97%AC-%ED%95%B4%EA%B2%B0%ED%95%98%EA%B8%B0)
