#바둑이 승차

def DFS(v):
    sum=0
    if v==m:
        for x in range(1,m+1):
            if li[x]==1:
                sum+=x
    else:
        li[v]=1
        DFS(v+1)
        li[v]=0
        DFS(v+1)
if __name__=="_main_":
    li={}
    weight = []
    n,m=map(int,input().split())

    for i in range(m):
        weight.append(input())

    for i in range(m):
        li[i]=weight[i]
    DFS(0)

#바둑이 승차
##부분집합을 만들어서 총합 구하기


if __name__=="_main_":
    c,n = map(int,input().split())
    a=[0]*n
    
