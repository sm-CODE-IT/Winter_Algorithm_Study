### 학습 정리한 내용

# 📍 최대공약수(GCD)를 구하는 방법 '유클리드 호제법'의 개념
## 최대공약수(GCD, Greatest Common Divisor)

> 두 자연수의 공통된 약수 중 가장 큰 수
> 

*최소공배수(LCM)는 **`두 자연수의 곱 / 최대공약수`**의 공식으로 구할 수 있다. 

## 유클리드 호제법

유클리드 알고리즘은 2개의 자연수의 최대공약수를 구하는 알고리즘 중 하나로, 두 수가 서로의 상대방 수를 나누어 원하는 수를 얻어내는 접근으로 이루어진다. 

## 접근 방식

***비교대상인 두 개의 자연수 a, b (단, a > b)에서 a를 b로 나눈 나머지를 r이라고 했을 때, GCD(a,b) = GCD(b,r)과 같고 r이 0이면, 그 때의 b는 최대공약수이다.*** 의 원리를 활용한다.

### 1. 반복문을 이용한 방법

```java
int gcd(int a, int b) {    
		int tmp, n;    // b가 a보다 큰 수가 되도록 swap    
		
		if (a < b) {        
				tmp = a;        
				a = b;        
				b = tmp;   
		}    

		while (b != 0) {  // b가 0이 되는 순간의 a를 GCD로 판단        
				n = a % b;        
				a = b;        
				b = n;    
		}    
		return a;
}
```

### 2. 재귀를 이용한 방법

```java
int gcd(int a, int b) {    
		if (b == 0) {        
				return a;    
		} else {        
				return gcd(b, a % b);    
		}
}
```

## 참고 자료

[[Algorithm] 유클리드 호제법 - 최대공약수(GCD) & 최소공배수(LCM)](https://velog.io/@hyojhand/%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C-%ED%98%B8%EC%A0%9C%EB%B2%95-%EC%B5%9C%EB%8C%80%EA%B3%B5%EC%95%BD%EC%88%98GCD-%EC%B5%9C%EC%86%8C%EA%B3%B5%EB%B0%B0%EC%88%98LCM)

[[Algorithm] 유클리드 호제법 - 최대공약수(GCD) 구하기](https://coding-factory.tistory.com/599)

# 📍 기본적인 아스키코드
## *️⃣ 문자 → 숫자 변환

```java
//== 문자 -> 숫자 변환 ==//
char alpha = sc.nextLine().charAt(0);
int alpha_num = (int) alpha;

System.out.println("입력 문자: " + alpha);
System.out.println("숫자 변환 이후: " + alpha_num);

// >>>
입력 문자: a
숫자 변환 이후: 97
```

## *️⃣ 숫자 → 문자 변환

```java
//== 숫자 -> 문자 변환 ==//
int num = sc.nextInt();
char num_alpha = (char) num;
System.out.println("입력 숫자: " + num);
System.out.println("문자 변환 이후: " + num_alpha);

// >>>
입력 숫자: 97
문자 변환 이후: a
```

# 📍 자바 진수 변환 (10진수 ↔ 2진수, 8진수, 16진수) - Integer API 사용
## 10진수 ➡️ 2진수, 8진수, 16진수

Integer 클래스의 toBinaryString(), toOctalString(), toHexString() 메소드를 사용하면 각각 2진수, 8진수, 16진수로 변환할 수 있다. 

```java
String binaryInt = Integer.toBinaryString(10); // 1010
String octalInt = Integer.toOctalString(10);   // 12
String hexInt = Integer.toHexString(10);       // a
```

## 2진수, 8진수, 16진수 ➡️ 10진수

Integer 클래스의 parseInt()를 사용하여 쉽게 10진수 변환이 가능하다. 

```java
int binToDec = Integer.parseInt(binaryInt, 2); // 10
int octToDec = Integer.parseInt(octalInt, 8);  // 10
int hexToDec = Integer.parseInt(hexInt, 16);   // 10
```


# 📍 에라토스테네스의 체 : 소수 판정
## 소수란?

> 1보다 큰 자연수 중 1과 자기자신만을 약수로 가지는 수
> 

### 에라토스테네스의 체

대량의 소수를 한꺼번에 빠르고 정확하게 판별할 수 있는 알고리즘으로, 가장 먼저 소수를 판별할 범위만큼 배열을 할당하고, 해당 값을 넣어준 후 하나씩 지워나가는 방식이다.

마치 체처럼 걸러낸다고 하여 다음과 같은 이름이 붙었고, 2부터 시작하여 특정 수의 배수에 해당하는 수를 배열에서 지워내고 남아있는 수를 소수로 판정한다. 

## 소수 구하기 알고리즘

### 1. 나누어떨어지는 수의 여부 체크

주어진 수에 대해 2부터 (자기자신-1)로 나누어 떨어지는 수가 하나라도 있다면 그 수는 소수가 아니다. 하지만 이는 처음부터 반복문을 돌아야 하므로 나누어 떨어지는 수가 큰 수일수록 속도가 저하된다. 

### 2. 제곱근 사용

1번 방식의 단점을 보완하고자, 소수의 수학적 성질을 이용하면 주어진 수의 제곱근까지만 나누어 떨어지는지 검사한 결과와 동일하다. 나누는 수에서 쌍을 이루지 않는 수가 존재할 때 그 최대는 N*N 즉, 제곱근이므로 제곱근까지만 판별할 경우 복잡도는 1차에서 절반만큼 줄어들게 된다. 

### 3. 에라토스테네스의 체 원리 이용

1,2번 방식은 단일 숫자에 대한 소수를 판정할 때 사용하고, 1~N까지의 수에서 모든 소수를 구하고자 할 때는 ‘에라토스테네스의 체’ 원리를 사용할 수 있다. 

```java
public class PrimeNumber {
    public static void main(String[] args) {

        int maxNum  = 100000;   // 판별할 대량의 소수 중 최댓값

        // 1. 배열 생성 후 초기화
        int[] arr = new int[100001];
        for (int i=2; i<=maxNum; i++) {
            arr[i] = i;
        }

        // 2. 2부터 시작하여 특정 수의 배수에 해당한다면 배열에서 지운다.(0으로 변경)
        for (int i=2; i<=maxNum; i++) {
            if (arr[i] == 0) continue;   // 이미 지워진 수라면 건너뛰기

            // 이미 지워진 숫자가 아닌 경우, 그 배수부터 건너뛰어서 시작
            for (int j=2*i; j<=maxNum; j+=i) {
                arr[j] = 0;
            }
        }

        // 3. 2부터 남아있는 수를 모두 소수라고 판별한다.
        for (int i=2; i<=maxNum; i++) {
            if (arr[i] != 0)
                System.out.println(arr[i]);
        }
    }
}
```

***빠른 소인수분해**

위 방식을 이용하면, 특정 수의 소인수분해를 아주 빠르게 구현할 수 있다. 
```java
//== 특정 수의 소인수분해 ==//
int n = 30;   // 30을 소인수분해 해보자!
for (int i=0; n>1; i++) {
    if (arr[i] != 0) {   // 해당 수가 소수인 경우
        while (n % i == 0) {
            System.out.println(i);  // 30의 소인수(소수)
            n /= i;   // 다시 그 수를 소수로 나눈 후에 다시 반복
        }
    }
}
```

## 참고 자료

[알고리즘 - 에라토스테네스의 체 : 소수(prime number)와 소인수분해](https://chanhuiseok.github.io/posts/algo-42/)

[[Algorithm] 에라토스테네스의 체](https://velog.io/@max9106/Algorithm-%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98-%EC%B2%B4)
