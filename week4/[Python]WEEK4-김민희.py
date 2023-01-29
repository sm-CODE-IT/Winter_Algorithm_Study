'''#가장 큰 수
a,b = map(int,input().split())
li=[]


# 각 숫자를 리스트에 저장
while True:
    c=a%10
    if a<10:
        li.append(c)
        break
    else:
        li.append(c)
    a=int(a/10)

li.reverse()
print(li)



c=len(li)
result=[]
max_li=max(li)
p=0
index=b
while len(result)!=c-b:
    print(li)
    print(len(li))
    print(b-len(result))
    for m,n in enumerate(li):
        if len(li)==(b-len(result)+1):
            for k in li:
                result.append(k)
            break

        if max_li==n and m<=index:
            result.append(max_li)
            del li[:m+1]
            index=b-len(result)
            if len(li)>0:
                max_li=max(li)
            continue

        elif max_li!=n:
            continue
        elif max_li==n and m>index:
            for x in li:
                if  x>=p:
                    p=x
            max_li=p
         
      
print(result)
'''


#-> 실패

#강의 설명
#앞에껄 지우고 자기가 앞으로 나가는 방식 -> 쉽게 구현 가능한 스택 자료구조
#기존에 내가 하던 방식은 전체 -> max를 찾아서 이용하는 방식

''''
stack -> last in first out
맨 마지막이 먼저 나온다. 
나오고 들어가는 곳이 동일하다

리스트를 이용!

앞에 숫자가 자기보다 작으면 pop을 시킴
만약 b번만큼 제거되지 못했다면
뒷 숫자들을 pop시킨다 -> 내림차순으로 push 됐기 떄문
'''

num,m= map(int,input().split())

num=list(map(int,str(num))) #string으로 해야 각각 접근 가능 -> int화 시킴

stack=[]

for x in num:
    while stack and m>0 and stack[-1]<x: #stack[-1] -> 제일 뒷 자료
        stack.pop()
        m-=1
    #내 앞에 있는 작은 자료들은 최대한 지워준다.
    stack.append(x)
    #다 지우지 못하는 경우 
if m!=0:
    stack=stack[:-m] #스택 자료의 순서가 거꾸로 -> -1,-2,-3....
    #-가 붙으면 [:-m]에서 인덱스가 -m인 자료까지 지워진다.

#스택이 낱개로 있음 -> 붙여주기
res=''.join(map(str,stack)) #-> join은 문자열만 가능. -> map으로 str화 시킴

#다른 방법
for x in stack:
    print(x,end="") #옆으로 붙여서 출력해줌.










#쇠막대기
a=input()

p=[]
q=[]
lazer=[]
for x,y in enumerate(a):
    if y=='(':
        p.append(x) 
    elif y==')':
        q.append((p.pop(),x))

for (i,j) in q:
   #홀수형 값만 검사? ->q.remove(i,j)라고 하니까 갑자기 돌아옴??
    if j-i==1:
        lazer.append((i,j))



cnt=0
result=[]

for i in q:
    cnt=0
    for j in lazer:
        print(i[0],j[0])
        if i[0]==j[0]:
            break

        if i[0] < j[0] and i[1]>j[1]:
            print("hi"+i[0])
            cnt+=1
        else:
            break

    result.append(cnt+1)

print(result)


#강의설명
#내 풀이와 달리 레이저를 따로 구분 -> ) 바로 앞에 (가 있으면 레이저
#레이저면 스택에 쌓인 (의 개수를 더하기 , 만약 레이저가 아닌 )가 오면 +1 해줌
#-> 윗 내용을 이해하기 위해선 그림 참조
#pop, push 계속 해보기

s=input()
stack=[]
cnt=0

for i in range(len(s)):
    if s[i]== '(':
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1] =='(':
            #stack.pop()
            cnt+=len(stack)
        else:
            
            #stack.pop()
            cnt+=1












#후위표기식 만들기

#강의 설명
a=input()
stack=[]
res='' #출력

for x in a:
    #십진수 인지 확인
    if x.isdecimal():
        res+=x #누적 ->출력
    else:
        if x=='(':
            stack.append(x)
        elif x=='*' or x=='/': #자기보다 연산 우선순위가 빠른 것들만 뽑아냄
            while stack and (stack[-1]=="*" or stack[-1]=='/') :#왼쪽을 우선처리
                res+=stack.pop() #스택의 최상단을 뽑아내서 누적
            stack.append(x)
        elif x=='+' or x=='-': #스택에 있는 것은 다 꺼낼 수 있음
            while stack and stack[-1]=='(': #( 가 있다는 것은 지금 연산자들이 괄호안의 연산식이라는 뜻, 
                #괄호 안의 연산식들은 스택에 있는 다른 연산들보다 우선순위가 높음
                res+=stack.pop()
            stack.pop()
        elif x==')':
             while stack and stack[-1]=='(':
                 res+=stack.pop() #사이 연산자들만 처리
             stack.pop() #닫는 괄호 처리
#스택에 남아 있을 경우
while stack:
    stack.pop()













#후위식 연산

a=input()
stack=[]
res=''

for x in a:
    if x.isdecimal():
        stack.append(x)
    else:
        if len(res)==0:
                res+=stack.pop()
                res+=x
                res+=stack.pop()
        else:
            res+=x
            res+=stack.pop()
print(res)

#강의 설명
# 10진수의 순서 고려 -> 맨 먼저 넣은 숫자가 연산을 당하는 객체
# 내 풀이처럼 계산식을 따로 만들지 않고 스택 안에서 바로 계산 

a=input()
stack=[]
res=''

for x in a:
    if x.isdecimal():
        stack.append(int(x)) #for 연산
    else:
        if x=='+':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2+n1)
        elif x=='-':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2-n1)
        elif x=='*':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2*n1)
        elif x=='/':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2/n1)
print(stack)













#공주 구하기
from collections import deque

m,n = map(int, input().split())
dq=[]
for i in range(1,m+1):
    dq.append(i)
dq = deque(dq)

while len(dq)!=1:
    for _ in range(n-1):
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft()

print(dq[0])

'''
큐
선입선출 구조(뒤쪽에서 넣고 앞쪽에서 꺼낸다)
스택은 넣고 빼는 곳이 동일함 -> 후입선출

덱 자료구조를 사용하여 큐 구현
덱은 앞, 뒤 쪽에서 pop push 가능
appendLeft, popLeft, 
'''
#12 -> pop하고 뒤쪽으로 appendright, 3은 제거 ->원형으로 도는 구조
#하나가 남을 때까지 반복
from collections import deque

n,k = map(int, input().split())
dq = list(range(1,n+1)) 
dq = deque(dq)

while dq:
    for _ in range(k-1):
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq)==1:
        print(dq[0])
        dq.popleft()












#응급실
from collections import deque
n,m=map(int,input().split())
dq=list(map(int,input().split()))

res = dq[m]
dq=deque(dq)

result=[]
cnt=0

for x in dq:
    for y in len(dq):
        if x<y:
            dq.popleft()
            dq.append(x)
            break
    else:
        dq.popleft() #제일 큰 값
        result.append(x)

# 같은 값일 경우 해결 -> 인덱스를 이용하면 될 듯



#강의 설명
'''n,m=map(int,input().split())
Q=[(pos,val) for pos,val in enumerate(list(map(int,input().split())))] #번째가 들어가도록 - 튜플 형태


Q = deque(q)
cnt=0
while True:
    cur=Q.popleft()
    if any(cur[1]<x[1] for x in Q) : #뒤 대기목록 중에 위험도가 높은지 확인
     #단 한 개라도 참이라면 any도 참. 위험도가 높은 것이 존재
        Q.append(cur)
    else:
        cnt+=1
        if cur[0]==m:
            break
print(cnt)'''













#교육과정 설계
from collections import deque
must=input()
num=int(input())

for x in range(num):
    dq=deque(must)
    study=input() 
    for x in study:
            if x in dq:
                if x!=dq.popleft():
                    print("NO")
                    break
                else:
                    if len(dq)==0:
                        break
                    else:
                        dq.popleft()
            else:
                continue
                        
    else:
        if len(dq)==0:
            print("YES")
        else:
            print("NO")

'''#강의 설명
from collections import deque
need = input()
n=int(input())
for i in range(n):
    plan = input()
    dq = deque(need)
    for x in plan :
        if x in dq:
            if x!=dq.popleft():
                print("#%d NO" %(i+1)) #순서가 틀림
                break
    else:
        if len(dq)==0: #수업계획서에 필수과목을 다 넣었는가
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))'''