#최대 점수 구하기


def DFS(L,s):
    global result
    if s>=m:
            return
    elif L==4:
        if s<m and s>result:
            result=s
        
    else:
        DFS(L+1,s+i[L])
        DFS(L+1,s)

if __name__=="_main_":
    n,m = map(int,input().split())
    score=[]
    time=[]
    result = -2147000000
    i,j=0
    for _ in range(n):
        i,j=map(int,input().split())
        score.append(i)
        time.append(j)
    DFS(0,0)

#강의 설명
'''
1번 문제 푼다 vs 풀지 않는다
5개를 다 적용해서 말단 노드를 만들었을 때 값이 크다면 갱신하는 식

'''

def DFS(L,sum,time):
    global res
    if time>m:
        return
    if L==n:
        if sum>res:
            res=sum
        else:
            DFS(L+1,sum+pv[L],time+pt[L])
            DFS(L+1,sum,time)

if __name__ =="_main_":
    n,m = map(int,input().split())
    pv = list()
    pt = list()
    for i in range(n):
        a,b = map(int,input().split())
        pv.append(a)
        pt.append(b)
    res = -2147000000
    DFS(0,0,0)


