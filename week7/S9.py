#경로 탐색
'''
1번 정점에서 갈 수 있는 노드로 가지뻗는 식으로 코드 작성

'''


def DFS(L):
    global cnt
    for i in range(n):
        for j in range(m):
            if g[i][j]==1 and j==5:
                cnt+=1
            if g[i][j]==1:
                DFS()
            else:
                break


if __name__=="_main_":
    n,m = map(int,input())
    g = [[0]*(n+1) for _ in range(m)]
    #인접 행렬 만들기
    for _ in range(m):
        a,b = map(int, input().split())
        g[a][b]=1
    cnt=0 #경우의 수



 #강의 설명
'''
한번 방문한 노드는 다시 방문하지 않는다 -> 체크 리스트 만들기
연결된 노드만을 찾는다. 

노드를 v==n까지 방문한 후 back할 때는 체크 했던 것을 다시 되돌려 놓아야 함

'''

def DFS(v): #v는 노드 번호
    global cnt
    if v == n: #종착지점
         cnt+=1
         for x in path:
             print(x,end=' ')
         print()
         
    else: 
        for i in range(1,n+1):
            #i가 노드 번호
            if g[v][i] == 1 and ch[i]==0:
                ch[i]=1 #방문했다
                path.append(i) #방문한 노드 출력
                DFS(i)
                path.pop() #넣었던 것 다시 pop
                ch[i]=0 #back해주는 부분
            
if __name__=="_main_":
    n,m = map(int,input().split())
    g =[[0]*(n+1) for _ in range(n+1)]
    ch=[0]*(n+1) #1~n개 써야 하니까 n+1
    #방향 그래프
    for i in range(m):
        a,b = map(int,input().split())
        g[a][b]=1

    cnt = 0
    #1번 노드 방문함
    ch[1]=1
    path=[]
    path.append(1)
    DFS(1)
    print(cnt)