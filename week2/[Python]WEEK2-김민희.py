####회문 문자열 검사
n=int(input()) #정수
for element in range(n):
    #모든 문자들을 소문자화
    element=input()
    element = element.lower()
    re = list(element) #함수와 변수명이 중복되었을 때 'list' object is not callable
    re.reverse()
    final = "".join(re)
    if final ==element: 
            print("YES")
    else:
            print("No")

#강의 풀이
import sys
sys.stdin = open("input.txt","r")
n=int(input()) #정수
for i in range(n):
        s=input()
        s=s.upper() #s를 대문자화
        size=len(s) #문자열의 길이
        for j in range(size//2): #두 개씩 비교해야 함.
                #파이썬은 인덱스 접근 -5, -4, -3, -2, -1fheh rksmd
                #s[j] s[-1-j]
                if s[j] !=s[-1-j]:
                        print("#%d NO" %(i+1))
                        break
        else: #정상적으로 끝남
                print("#%d YES" %(i+1))

        #더 짧은 코드 -> 코테에서  직접 비교해보라고 시키기도 함!(reverse말고)
        # if s==s[::-1] -> s가 거꾸로 reverse된 문자열
        if s==s[::-1]:
                print("#%d YES" %(i+1))
        else:
                print("#%d NO" %(i+1))



#####숫자만 추출
#약수 추출
def find(x):
    cnt=0
    for i in range(1,x+1):
        if x%i==0:
            cnt+=1
    return cnt

str="Akdj0Gk1dgdgdAGSGAG3DGGA45GAGADGDGdjADG2SDGkdj0f"
str.upper()
li=[] #숫자를 담을 리스트 
result=0

#리스트화
str=list(str)

#알파벳과 숫자 분류
for i in str: #'<' not supported between instances of 'str' and 'int'
    j=ord(i) #숫자는 48부터 시작
    if j<65:
        li.append(int(i)) #숫자를 다시 문자열로 캐스트

#0은 없애주고 
for i in li:
    if i==0:
        li.remove(i)
    else:
        break


#각 숫자들을 합치는 작업
for i,j in enumerate(li): #인덱스가 먼저 나온다.
    result += j*10**(len(li)-i-1)

print(result)
print(find(result)) #name 'find' is not defined



#강의 풀이
import sys
sys.stdin("input.txt","r")
s = input()

res=cnt=0 #숫자 추출
for x in s: #문자열 s의 문자를 하나씩 for문으로 돈다
    if x.isdecimal(): #isdecimal은 0~9만 , isdigit은 모든 숫자(예로 들어 2의 2승..)인지 검사하는 함수
        res = res*10 + int(x) #다음과 같은 방식을 사용하면 자동적으로 첫번째 0은 무시한다.
print(res)

for x in range(1,res+1): #res까지 돌아야 한다,숫자화 시키는 방법
    if res%x ==0:
        cnt+=1
print(cnt)
 

 #####카드 역배치
li=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#리스트를 거꾸로 하는 함수
def solution(x,y,li):
    cnt=0
    li2=[]
    for i in li:
        li2.append(i)
 

    for i in range(x-1,y): #range()범위 실수 조심
         #값을 바꿀때는 값을 저장하는 매개변수 따로 설정하는거 잊지말기
        li[i]=li2[y-1-cnt]
        cnt+=1
    #원본 리스트 값 바꾸기
    return li

li=solution(13,17,li)
li=solution(2,19,li)
li=solution(1,2,li)
li=solution(3,19,li)
li=solution(1,1,li)
li=solution(1,9,li)
li=solution(11,16,li)
li=solution(5,6,li)
li=solution(1,3,li)
li=solution(1,9,li)
print(li)

#강의 풀이
import sys
sys.stdin("input.txt","r")
a=list(range(21)) #리스트를 만들고

for _ in range(10): #10바퀴를 돈다
    s,e=map(int,input().split())
    for i in range((e-s)//2):
        a[s+i],a[e-i]=a[e-i],a[s+i] #파이썬의 swap방법

a.pop(0) #괄호 안에 들어가는 값은 인덱스 개념으로 접근
#0을 먼저 없애고 리스트를 만들면 -> 모든 인덱스에 -1을 해줘야 함 -> 복잡

for x in a:
    print(x,end=" ") #옆으로 출력



##### 두 리스트 합치기
list1=[1,3,5]
list2=[2,3,6,7,9]

'''for i in list2:
    list1.append(i)

print(sorted(list1))
'''
#강의에서 무엇을 중점적으로 다루지?

#강의풀이 
#이 문제는 리스트를 더하기 연산자를 이용하여 합치고 sort()함수로 정렬 -> ㄴㄴ
# sort() => nlogn
# 정렬되어 있는 것을 활용 -> n번만 돌면 된다.

#강의에서 말한 방법대로 만든 내 코드
p1=p2=0 #포인터 변수는 일단 0으로 두고
list3=[]
for _ in range(max(len(list1),len(list2))) :
    if p1<=len(list1)-1 and p2<=len(list2)-1:
        if list1[p1]< list2[p2] :
            list3.append(list1[p1])
            p1+=1
        elif list1[p1] ==list2[p2]:
            list3.append(list1[p1])
            list3.append(list2[p2])
            p1+=1
            p2+=1
        else:
            list3.append(list2[p2])
            p2+=1
    else:
        break

# 남은 리스트를 붙이는 작업 - error ->solve
if p1<=len(list1)-1:
    for x in range(p1,len(list1)):
        list3.append(list1[x])
elif p2<=len(list2)-1:
    for x in range(p2,len(list2)):
        list3.append(list2[x])

print(list3)

#강의 코드
import sys
sys.stdin = open("input.txt","r")
n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))

p1=p2=0
c=[]
while p1<n and p2<m: #for + if문 합친 역할
    if a[p1]<=b[p2]: #어차피 b도 정렬이 되어 있다. p1의 다음 인덱스의 값보다 작을 때 p2인덱스 값이 c에 들어가도 문제 없다.
        c.append(a[p1])
        p1+=1
    else:
        c.append(b[p2])
        p2+=1

if p1<n:
        c=c+a[p1:]
if p2<m:
        c=c+b[p2:]
for x in c:
    print(x,end=" ")



#####수들의 합
li=list(map(int,input().split()))
N=int(input())
M=int(input())
print(li)
cnt=answer=0
for i in range(M):
    cnt=li[i]
    if cnt==N:
        answer+=1
    for j in range(i+1,M): #range없이 사용 -> i 이후로의 배열 값만을 담은 리스트를 구할 수가 없었다.
        cnt+=li[j]
        if cnt == N:
            answer+=1
            break
        elif cnt>N:
            break
print(answer)

#강의 풀이




#####격자판 최대합
#어떻게 값을 받는지에 따라 다를듯
#list로 받는다고 생각할까?

''' import sys
sys.stdin = open("input.txt","r")
'''
n= int(input())
a=[list(map(int,input().split())) for _ in range(n)] #map이 한 줄을 읽어서 list화 시킴

#2차원 리스트임
res=result=0 #가장 큰 값을 담을 변수

#각 행의 합
for x in a:
    res=sum(x)
    if res>result:
        result=res

#각 열의 합
for i in range(n):
    for b in range(n):
        res=0
        for c in range(n):
            res+=a[c][b]
        if res>result:
            result=res
res=0
#각 대각선의 합
for i in range(n):
    res+=a[i][i]
    if res>result:
        result=res
res=0
for i in range(n):
    res+=a[n-1-i][i]
    if res>result:
        result=res

print(result)
#다른 방식을 원하는 것 같다.. -> 통합?


#강의 풀이
import sys
sys.stdin=open("input.txt","r")
n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
largest = -2147000000
#행렬의 합 -> 합침
for i in range(n):
    sum1=sum2=0
    for j in range(n):
        sum1+=a[i][j]
        sum2+=a[j][i]
    if sum1>largest:
        largest=sum1
    if sum2>largest:
        largest=sum2
#대각선 합
sum1=sum2=0
for i in range(n):
    sum1+=a[i][i]
    sum2+=a[i][n-i-1]
    if sum1>largest:
        largest=sum1
    if sum2>largest:
        largest=sum2
print(largest)





#####사과나무
n= int(input())
li=[list(map(int,input().split())) for _ in range(n)]

result=0 #수확한 사과의 개수
stp=n//2
cnt=n//2-1

for a in range(n//2+1):
            for i in range(a+1):
                result+=li[a][stp+i]
                print(li[a][stp+i])
                if i>0:
                    result+=li[a][stp-i]
                    print(li[a][stp-i])

#왜 자꾸 30을 빼먹을까 -while
while cnt>=0:
    for a in range(n//2+1,n):
        #for cnt
            for i in range(cnt+1):
                print(cnt)
                result+=li[a][stp+i]
                print(li[a][stp+i])
                if i>0:
                    result+=li[a][stp-i]
                    print(li[a][stp-i])
                
            cnt-=1
        

print(result)

#강의 풀이
import sys
sys.stdin=open("input.txt","r")
n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
res=0
s=e=n//2
for i in range(n):
    for j in range(s,e+1):
        res+=a[i][j]
    if i<n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1
print(res)





#####곶감
n= int(input())
li=[list(map(int,input().split())) for _ in range(n)]
m=int(input())
li2=[]
for i in range(m):
    h,t,k=map(int,input().split())
    for j in range(n):
           li2.append(li[h-1][j])
    if t==0:
        for j in range(n):
            li[h-1][j]=li2[(j+k)%n]
    else:
        for j in range(n):
            li[h-1][j]=li2[(n-j-k)%n]
print(li)

'''cnt=n//2 #간격
stp=n//2
result=0

for a in range(stp):
    while cnt>=0:
        for b in range(cnt+1):
            result+=li[a][stp+cnt]
            if b>0:
                result+=li[a][stp-cnt]
        cnt-=2

cnt2=0
for a in range(stp+1,n):
    while cnt2<=n//2:
        for b in range(cnt2+1):
            result+=li[a][stp+cnt2]
            if b>0:
                result+=li[a][stp-cnt2]
        cnt2+=2

print(result)'''

s=0
e=n
result=0
for i in range(n):
    for j in range(s,e):
        result+=li[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1


print(result)
       
        
#강의 풀이
#pop,inset를 활용하여 값을 이동
'''for i in range(m):
    h,t,k=map(int,input().split())
    if t==0 : 
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            a[h-1].insert(0,a[h-1].pop())'''











