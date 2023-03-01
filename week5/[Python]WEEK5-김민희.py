#단어 찾기
n=int(input())
voca=[]
use=[]
for _ in range(n):
    voca.append(input())

for _ in range(n-1) :
    use.append(input())

#기존에 쓰던 방식
for i in use:
    for j in voca:
        if i==j:
            break

    else:
        print(i)

# 생각한 방식 -> 정렬?

voca=voca.sort()
use = use.sort()

for i in range(n-1):
    if voca[i]!=use[i]:
        print(voca[i])

#강의 
'''
dict 사용 -> key(정수, 문자열도 가능) : 인덱스 역할
key의 value값을 1로 체크 => key의 value값을 0으로 바꿨을 때 1인것
'''
n= int(input())
p=dict()

for i in range(n):
    word=input()
    p[word]=1       #인풋 받은 값을 딕셔너리의 키로 사용
for i in range(n-1):
    word= input()
    p[word]=0
for key,val in p.items(): #딕셔너리는 키와 값 for문에서 모두 접근 가능
    if val==1:
        print(key)
        break










#아나그램
word1=input()
word2=input()

p=dict() #1번 문자열
p2=dict() #2번 문자열
for i in word1:
    if i in p: #없는 키 값을 가져오라고 하면 에러 발생 -> 딕셔너리에 키가 있는지 확인 필수
        p[i]+=1
    else:
        p[i]=1
for i in word2:
    if i in p2:
        p2[i]+=1
    else:
        p2[i]=1

for key1,val1 in p.items():
    for key2,val2 in p2.items():
        if key1==key2 and val1 == val2:
            break
    else:
        print("No")
        break
else:
    print("Yes")


#강의 설명
'''
기존 값이 없다면 -> 딕셔너리 +=1 하면 안됨
str1.get('A',0) ->a라는 키 값이 없다면 0, 있다면 값을 리턴
str1[A]=str1.get('A',0)+1
'''

a=input()
b=input()
str=dict()
str2=dict()

for x in a:
    str[x]=str.get(x,0)+1
for x in b:
    str[x]=str2.get(x,0)+1

for i in str.keys(): #딕셔너리의 키에 접근 가능
    for i in str2.keys():
        if str[i]!=str2[i]:
            print("No")
            break
    else:
        print("No")
        break
else:
    print("Yes") #정상 아나그램

#개선 코드
for x in a:
    str[x]=str.get(x,0)+1
for x in b:
    str[x]=str.get(x,0)-1 #원상복귀 -> 다 0으로 바꿈

for x in a:
    if str.get(x)>0: #문자키의 값이 0이 아닐때 -> ㅇ나그램이 아님
            print("NO")
            break
else: #정상 동작
        print("YES")

#또 다른 개선 코드
for i in str.keys():#딕셔너리의 키값에 접근했을 때
    if i in str2.keys():
        if str[i]!=str2[i]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")
 


 #리스트 해쉬 -> 일반 리스트 형식

 #0으로 초기화
str11=[0]*52 #알파벳이 총 52개인걸 이용
str22=[0]*52

for x in a:
    if x.isupper() : #대문자 검사
        #아스키 넘버로 바꿔주는 함수 ord()
         str11[ord(x)-65]+=1 #대문자 아스키 코드값 65~90 -> 65를 0으로
    else:
        str11[ord(x)-71] +=1
for x in b:
    if x.isupper() : #대문자 검사
         str22[ord(x)-65]+=1 #대문자 아스키 코드값 97~122
    else:
        str22[ord(x)-71] +=1

for i in range(52): #str11 != str22도 사용 가능
    if str11[i] != str22[i]:
        print("NO")
        break
else:
    print("Yes")












#최소힙
'''
최소힙 -> 이진트리를 이용하여 make
트리에 대한 기본적인 설명 

최소힙
부모보다 자식의 값이 커야 한다. -> 값을 넣었을 때 부모보다 값이 작으면 올라가기
입력값은 가장 높은 레벨로 삽입됨
부모랑 비교하면서 위로 올라감 -> 업힙


아래로 내려간다 -> 다운 힙

pop하면 현재 가장 작은 값인 루트 값이 빠져나옴
pop되는 순간. "가장 높은 레벨"의 오른쪽 값을 루트에 삽입
이 후 최소힙 과정을 거침 -> 두 자식 중 가장 작은 값과 swap => 이게 다운힙

최소힙 완성



'''
#heapq가 파이썬에서는 힙
import heapq as hq

a=[]
while True:
    n=int(input())
    if n==-1:
        break
    if n ==0 :
        if len(a) ==0:
            print(-1)
        else: #힙 자료구조에 값이 있다
            print(hq.heappop(a)) #함수 -> a에서 자료를 pop -> root 노드 값
    else:
        hq.heappush(a,n) #a에 n을 최소힙 구조로 넣는다.(트리 형태) 









#최대힙
''''
부모 노드가 자식 노드보다 항상 크다
루트 노드에는 가장 큰 값이 존재

최소힙 코드에서 최대힙을 나타내기 위해서는 -> 입력하는 값의 부호를 바꿔버리기
'''
import heapq as hq

a=[]
while True:
    n=int(input())
    if n==-1:
        break
    if n ==0 :
        if len(a) ==0:
            print(-1)
        else: #힙 자료구조에 값이 있다
            print(-hq.heappop(a)) #원래 부호값으로 바꾸기
    else:
        hq.heappush(a,-n) #부호 바꾸기
















#재귀함수와 스택
''''
재귀함수는 반복문의 다른 형태


'''
def DFS(x):
    if x>0:
        DFS(x-1)
        print(x,end=" ") #프린트함수의 위치에 따라 출력되는 순서가 다르다


'''
메인에서 DFS가 호출되자마자 스택 메모리에 정보가 저장됨
-> 매개변수, 지역변수, 반환되어야 할 주소(복귀주소)

DFS(3)이 동작하자마자 - 스택에 위 정보 저장(DFS(1),DFS(2),DFS(3) 묶음별로 -> 스택 프레임 ) - DFS(2)가 동작 -....
DFS(0)은 호출되자마자(스택에 정보 저장 ) 조건에 안맞아서 종료됨 -> 스택 프레임도 지워짐
단 복귀주소에 따라 DFS(1)로 복귀. 따라서 그 다음 문장인 print() 실행
DFS(1) 종료 - 복귀주소에 따라 DFS(2)에서 실행 -> 그 다음 문장인 print(x,end=" ") 실행
...
따라서 1,2,3 호출

재귀함수는 스택을 활용해서 자료구조를 실행


'''


if __name__ == "_main_ ": #메인 함수와 재귀함수의 구분. -> 이 스크립트가 실행되면 main을 찾아서 제일 먼저 실행
    n=int(input())
    DFS(n)
















n=int(input())

def two(n):
    li=[]
    li.append(n%2) #local variable 'li' referenced before assignment
    if n//2 >=2:
        two(n//2)
    else:
        return li
if __name__=="_main_":
    print(two(n))

#재귀함수를 이용한 이진수 출력

def DFS(x):
    if x==0:
        return
    else:

        DFS(x//2)
        print(x%2,end=" ") #스택을 사용하므로 순서를 바꿔주면 거꾸로 출력됨

if __name__=="_main_":
    n=int(input())
    DFS(n)



'''
항상 스택은 스택의 최상단이 작동 중임

'''















#이진트리 순회

'''
깊이 우선 탐색 -> 재귀 이용
전위 순회 : 부 - 왼 - 오 순서로 출력
중위 순회 : 왼 - 부 -오 순서
후위 순회 : 왼 - 오 - 부

'''
def DFS(v):
    if v>7:
        return
    else:
        print(v) #전위 순회 -> 왼쪽 오른쪽 가기전에 본연의 작업을 끝내고 넘어감, 많이 쓰임
        DFS(v*2)
        print(v)# 중위 순회
        DFS(v*2+1)
        print(v) #후위 순회 -> 대표적인 예 병합 정렬


if __name__=="_main_":
    DFS(1)



















#부분집합 구하기

def DFS(n):
    

#강의 설명

'''
D(1)에서 시작해서 1을 부분집합으로 사용하는 경우와 아닌 경우로 노드 나누기 -> 3까지
상태 트리 활용
'''
def DFS(v): #원소의 개수(노드의 개수)
    if v==n+1: # 종착점이 되었을 때 -> 종료지점이라서 출력.
        for i in range(1,n+1):
            if ch[i]==1:
                print(i,end=" ")
        print() #줄바꿈
        
    else:
        ch[v]=1 #체크가 들어가면 사용
        DFS(v+1)
        ch[v]=0 #사용하지 않겠다
        DFS(v+1)
    #1이라고 되어 있는 것만 출력
 

if __name__=="_main_":
    n=int(input())
    ch=[0]*(n+1) #체크 변수
    DFS(n)




















#합이 같은 부분집합

'''
모든 부분집합의 합을 sum이라는 변수에 저장

부분집합을 만들면 -> 내 원소들을 포함하지 않는 부분집합도 생성됨
total - sum -> 또 다른 부분집합의 합 => 둘이 같냐 아니냐
'''
def DFS(L,sum): #L번 인덱스를 부분집합에 포함하겠다, 레벨의 의미도 있음
    #인덱스를 포함하겠다 vs 포함하지 않겠다로 노드를 나눈다
    if sum>total//2: #내가 만든 부분집합이 토탈//2보다 크면 가지를 뻗을 필요가 없다
        return
    if L==n:
        if sum==(total-sum):
            print("YES")
            sys.exit(0) #프로그램 종료 -> 함수가 아닌 프로그램 자체
        else:
            DFS(L+1,sum+a[L])
            DFS(L+1,sum) #a[L]을 사용하지 않겠다



if __name__=="_main_":
    n=int(input())
    a=list(map(int,input().split()))
    total = sum(a)
    DFS(0,0)
    print("NO") #절반인 경우가 없어서 프로그램이 돌고 끝나버렸다

'''
시간복잡도 줄이기
sum이 토탈의 절반을 넘어간다면, 같아질리가 없음
굳이 밑으로 내려갈 필요가 없다-> 같은 경우가 존재하지 않음

sum==total/2 라고 하면 안됨
if sum>total//2:
    return

'''















#전역변수와 지역변수

'''
메인 스크립트에 생성되면 -> 전역변수
전역변수는 모든 함수가 접근할 수 있다.

print(cnt)에서 cnt가 지역변수인지 확인 -> 아니러라 -> 전역변수인지 확인 순

'''
def DFS1():
    cnt=3 #지역변수가 우선. 3을 출력한다.
    print(cnt)

def DFS2():
    #전역변수라고 생각하고cnt를 만들었음 -> 로컬 변수가 안되려면?
    global cnt #cnt는 로컬변수라고 선언x, 전역변수로만 생각
    if cnt == 5:
        cnt+=1 #cnt라는 지역변수가 생김. 근데 cnt값 자체가 없음. -> 에러
        print(cnt)

if __name__=="_main_":
    cnt=5
    DFS1()
    DFS2()
    print(cnt)

#리스트 경우

def DFS():
    a[0]=7 #로컬 리스트 생성이 아닌 전역리스트로 생각하고 작동
    #a=[7,8] #이 때는 로컬 리스트
    #a=a+[4] #이 때 a는 로컬리스트 -> a라는 리스트는 없다. -> 할당 못함
    #이 때 a를 전역으로 만드려면 global a 구문 추가
    print(a)

if __name__=="_main_":
    a=[1,2,3]
    DFS()
    print(a)









