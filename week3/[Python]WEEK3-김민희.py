#이분 검색
n=int(input())
m=int(input())

a=list(map(int,input().split()))
a=sorted(a)
pl=0
pr=len(a)-1

while True:
    pc=(pl+pr)//2
    if a[pc]==m:
        print(pc+1)
        break
    elif a[pc]<m:
        pl=pc+1
    else:
        pr=pc-1


#강의 내용
'''
이분 검색 -> 정렬된 상황
lt, rt 가운데 mid를 설정 -> mid=(lt+rt)//2
a[mid]<m -> 
rt=mid -1

a[mid]>m ->
lt=mid+1
한번 할 때마다 절반씩 줄어듦
'''
import sys
sys.stdin=open("input.txt","r")
n,m=map(int,input().split())
a=list(map(int, input().split()))
a.sort()
lt=0
rt=n-1
while lt<=rt: 
    mid=(lt+rt)//2
    if a[mid]==m:
        print(mid+1)
        break
    elif a[mid]>m:
        rt=mid-1
    else:
        lt=mid+1
        






#랜선 자르기
n,m=map(int,input().split())
a=list(map(int, input().split()))
a.sort()
rt=len(a)-1
while True:
    mid=rt//2
    number=0
    for num in a:
        number+=num//a[mid]
    if number>=m:
        print(a[mid])
        break
    else:
        rt=mid-1
        continue

#강의 설명
'''이분검색 사용
랜선 길이 1~802로 잡음
401cm로 나눴을 때는 11개 이상의 랜선이 나오지 못한다. -> 범위 바꿔주기 1~ 400
이분검색을 계속해서 수행
'''
def Count(len):
    cnt=0
    for x in Line:
        cnt+=(x//len)
    return cnt

k, n =map(int, input().split())
Line=[]
res=0
largest=0
for i in range(k):
    tmp=int(input())
    Line.append(tmp)
    largest=max(largest,tmp)
lt=1
rt=largest
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=n:
        res=mid
        lt=mid+1
    else:
        rt=mid-1
print(res)








#뮤직비디오
k,n=map(int,input().split())
a=list(map(int, input().split()))

Line=[]
result=0
lt=0
for i in range(k):
    tmp=int(input())
    Line.append(tmp)
    largest=max(largest,tmp)
rt=largest
while lt<=rt:
    mid=(rt+lt)//2


#강의 설명
def Count(capacity):
    result=0
    num=1
    for i in Music:
        result+=i
        if result > capacity:
            num+=1
            result=i
        else:
            result+=i
    return num
            
n,m=map(int, input().split())
Music = list(map(int, input().split()))
lt=1
rt=sum(Music)
res=0
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)<=m:
        res=mid
        rt=mid-1
    else:
        lt=mid+1
print(res)











#마구간 정하기
n,m=map(int,input().split())
a=list(map(int, input().split()))

a.sort()
li=[]
for i in range(0,len(a)-1):
    li.append(a[i+1]-a[i])
summ=0
for i in li:
    summ+=i #합
lt=1
rt=summ



def Count(capacity):
    result=0
    cnt=0
    for i in li:
        result+=i
        if result>capacity:
            cnt+=1
            result=i
        else:
            result+=i
    return cnt
    
while lt<=rt:
    mid=(rt+lt)//2
    if Count(mid)<=m:
        res=mid
        rt=mid-1
    else:
        lt=mid+1

answer=0
for i in range(0,res):
    answer+=li[i]
print(li)
print(res)
print(answer)

#강의 설명
# 가장 가까운 말의 거리를 기준으로 ! -> 배치할 수 있는 말의 개수로 lt와 rt값 바꾸기
def Count(len):
    cnt=1
    ep=Line[0]
    for i in range(1,n):
        if Line[i]-ep>=len:
            cnt+=1
            ep=Line[i]
    return cnt

n,c=map(int,input().split())
Line=[]
for _ in range(n):
    tmp=int(input())
    Line.append(tmp)
Line.sort()
lt=1
rt=Line[n-1]

while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=c:
        res=mid
        lt=mid+1
    else:
        rt=mid-1










#회의실 배정
n=int(input())
meeting=[]
for i in range(n):
    s,e=map(int,input().split())
    meeting.append((s,e))
meeting.sort()
print(meeting)
num=0
store=[]
res=0
for i,j in enumerate(meeting):
    num=1
    res=j[1]
    print("res is")
    print(res)
    for k in range(i+1,n):
        if res==meeting[k][0]:
            num+=1
            res=meeting[k][1]
            print(meeting[k])
        store.append(num)
            
print(max(store))

#강의 설명
'''그리드 알고리즘이란
문제를 풀어나가는 단계에서 그 단계에서 가장 좋은 것을 선택
판별 -> 정렬
그리드 알고리즘은 정렬과 함께한다.
'''
'''
끝나는 시간을 기준으로 정렬
끝나는 시간보다 시작하는 시간이 크거나(이걸 놓침) 같으면 됨

'''
n=int(input())
meeting=[]
for i in range(n):
    s,e=map(int,input().split())
    meeting.append((s,e))
meeting.sort(key=lambda x: (x[1],x[0])) #정렬순위를 x[1] 위주로
et=0
cnt=0
for s,e in meeting:
    if s>=et:
        et=e
        cnt+=1
print(cnt)










#씨름 선수
#내 풀이 -> 이중 for문 비효율적
n=int(input())
li=[]
for i in range(n):
    s,e=map(int,input().split())
    li.append((s,e))

num=n
for s,e in li:
    for k,m in li:
        if s<k and e<m:
            num-=1
        else:
            print(s,e,k,m)

print(num)

#강의 설명
#몸무게 최대값 찾아가는(갱신) 방식
'''
183 65
181 60
180 70
172 67
170 72
'''
n=int(input())
li=[]
for i in range(n):
    s,e=map(int,input().split())
    li.append((s,e))

li.sort(reverse=True) #내림차순
largest=0
cnt=0

for x,y in li:
    if y>largest:
        largest=y
        cnt+=1
print(cnt)










#창고 정리
#그리디 알고리즘 -> 정렬 이용
n=int(input())
a=list(map(int,input().split()))
m=int(input())

a.sort()
for _ in range(m):
    
    a[len(a)-1]-=1
    a[0]+=1
    a.sort()

#a.sort()를 맨위에 두면 답 오류 -> 정렬되지 않은 상태로 차이가 구해짐

print(a[len(a)-1]-a[0])

#강의설명
L=int(input())
a=list(map(int,input().split()))
m=int(input())

a.sort()
for _ in range(M):
    a[0]+=1
    a[L-1]-=1
    a.sort()
print(a[L-1]-a[0])










 #침몰하는 타이타닉
from collections import deque
n,m=map(int,input().split())
a=list(map(int,input().split()))
#50 60 70 90 100
a.sort(reverse=True) #오름차순
result=0
cnt=0
for i in range(n):
    if a[i]<=m:
        result=a[i]
    for j in range(n-i-1):
        if result+a[i+j]<=m:
            result+=a[i+j]
            print(result)
        else:
            cnt+=1
            break
print(cnt)

#강의 설명
#가장 큰 몸무게의 사람이 같이 탈 수 있는 사람은 가장 몸무게가 작은 사람일 확률이 높다
#가장 작은 몸무게와 가장 큰 몸무게 비교 -> 같이 탈 수 있는지. 없으면 그 다음으로 가장 큰 몸무게와 비교
#타고 나갈 때마다 보트 수 증가

n,limit=map(int,input().split())
p=list(map(int,input().split()))

p.sort()
p=deque(p) #덱 자료형으로 변환
cnt=0 #구명 보트 개수 카운팅
while p: #비어있으면 거짓, 멈춤
    if len(p)==1:
        cnt+=1
        break
    if p[0]+p[-1]>limit: #리스트의 마지막 자료 -> -1
        p.pop()#구명보트 타고 탈출
        cnt+=1
    else:
        p.popleft() #뒷 자료들이 앞으로 땡겨짐 -> 안하기 위해서 덱 이용.(포인터가 이동)
        p.pop()
        cnt+=1
    #만약 자료가 1개만 남게 된다면, p[0]+p[-1]-> 한명의 몸무게 x2가 됨
    #만약 그렇게 되더라도 p.pop(0)을 하고나서도 p.pop() -> 논리적 오류
print(cnt)











#증가수열 만들기
n=int(input())
a=list(map(int,input().split()))

num=a[0]
a.pop(0)
cnt=1
result="L"
while a:
    if num+1<=a[-1] and num+1<=a[0]:  
        if a[-1]<a[0]:
            result+='R'
            cnt+=1
            num=a[-1]
            a.pop()
            print(a)
            print(num)
        elif a[-1]>a[0] :
            result+='L'
            cnt+=1
            num=a[0]
            a.pop(0)
            print(a)
            print(num)  
    elif num+1<=a[-1]:
            result+='R'
            cnt+=1
            num=a[-1]
            a.pop()
            print(a)
            print(num)
    elif num+1<=a[0] :
            result+='L'
            cnt+=1
            num=a[0]
            a.pop(0)
            print(a)
            print(num)      
    else:
        break
print(cnt)
print(result)

#강의설명
#lt와 rt라는 포인터 변수
#last에 마지막항을 저장
#(2,L), (3,R) 정렬하면 (2,L)이 작으므로 last에 2를 저장
#lt와 rt가 last보다 작다면 break

lt=0
rt=n-1
last=0
res=""

tmp=[]
while lt<=rt:
    if a[lt]>last:
        tmp.append((a[lt],'L')) #튜플 형식으로 저장
    if a[rt]>last:
        tmp.append((a[rt],'R'))
    tmp.sort()
    if len(tmp)==0:
        break #다 last보다 작을 때
    else:
        res=res+tmp[0][1]
        last=tmp[0][0] 
        if tmp[0][1]=='L':
            lt+=1
        else:
            rt-=1
    tmp.clear()

print(len(res))
print(res)















