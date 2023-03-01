#조합구하기

'''
이 문제 꼭 잘 기억해두기
상태트리가 다른 문제와 다름.

D(0,1(start))가 밑으로 내려갈수록 start부분이 +1,
그런데 가지도 start+1부터 시작. for문이 start부터 돈다.

'''
def DFS(L,s):
    global cnt
    if L == m:
        for j in range(L):
            print(res[j],end=' ')
            print()
            cnt+=1
    else:
        for i in range(s,n+1) :#가지가 s부터 n까지
            res[L]=i
            DFS(L+1,i+1)

            
if __name__=="_main_":
    n,m = map(int,input().split())
    res=[0]*(n+1)
    cnt=0
    DFS(0,1)
