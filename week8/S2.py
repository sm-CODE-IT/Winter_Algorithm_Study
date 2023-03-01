#휴가


def DFS(L,day,sum):
    global res
    if day>n:
        return
    if L==n:
        if sum>res:
            res = sum
    else:
        DFS(L+1,day+day[L],sum+benefit[L])
        DFS(L+1,day,sum)

if __name__ =="_main_":
    n=int(input())
    day =[]
    benefit = []
    res=-2147000000
    for _ in range(n):
        i,j=map(int,input().split())
        day.append(i)
        benefit.append(j)
#확인해보기 

#강의 설명

def DFS(L,sum):
    global res
    if L==n+1:
        if sum>res:
            res = sum
    else:
        if L+T[L]<=n+1:
            DFS(L+T[L],sum+P[L])
        DFS(L+1,sum)

if __name__=="_main":
    n=int(input())
    T=list()
    P=list()
    for i in range(n):
        a,b = map(int,input().split())
        T.append(a)
        P.append(b)
    res=-2147000000
    T.inset(0,0) #T리스트의 1번째 인덱스에 값을 넣을것 ㅇㅇ
    P.insert(0,0)
    DFS(1,0)
