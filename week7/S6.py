#수들의 조합


def DFS(L,s):
    sum=0
    global cnt
    if L==m:
        for i in range(m):
            sum+=res[i]
        if sum%6==0:
            cnt+=1
    else:
        for j in range(s,n+1):
            res[L]=li[j]
            DFS(L+1,j+1)




if __name__=="_main_":
    n,m=map(int,input().split())
    li = list(map(int,input().split()))
    k=int(input())
    res=[0]*(n+1)   #숫자 보관
    cnt=0 #가지 갯수 세기
    DFS(0,1)
    print(cnt)

#그림 그리면서 풀자. D(0,1) - D(1,2)...


#수들의 조합
#강의 설명
'''
DFS(0(level),0(start),0(sum))
sum + a[i]

'''

def DFS(L,s,sum):
    if L == k:
        if sum%m==0:
            cnt+=1
    else:
        for i in range(s,n): #list a는 0~n-1까지 값이 있으므로
            DFS(L+1,i+1,sum+a[i])

if __name__=="_main_":
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    m = int(input())
    cnt =0
    DFS(0,0,0)
