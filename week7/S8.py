#인접 행렬
'''
인접 행렬이란 그래프에 노드간의 간선이 존재한다면, 해당 간선의
시작 노드와 끝 노드 사이의 위치에 인접 행렬에서 1을 채워 넣는다. 
그래프 간의 간선이 존재하지 않는다면 인접 행렬에서는 0을 채워 넣는다.


노드와 간선의 집합을 그래프라고 한다
간선 중에서 방향이 설정된 것 : 방향 그래프
간선의 값까지 설정 - 가중치 방향 그래프

무방향 그래프 : 쌍방으로 갈 수 있다.
인접행렬은 항상 행번호에서 열번호로 이동한다 생각하기
ex) g[a][b] = 1, g[b][a]=1 


'''

'''
무방향 그래프 예시
55
12
13
24
34
45

n,m = map(int,input().split())
g=[[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    g[a][b]=1
    g[b][a]=1

for i in range(1,n+1):
    for j in range(1,n+1):
        print(g[i][j], end=' ')
    print()




'''

#가중치 방향 그래프
'''
1번 노드->2번 노드로 가는 간선의 가중치가 7이면
1 2 7로 표현


'''
n,m = map(int,input().split())
g=[[0]*(n+1) for _ in range(n+1)] #그래프 만들려면 [0]*(n+1)로 해야 n열을 가진 그래프가 만들어지는 듯??
for i in range(m):
    a,b,c = map(int,input().split()) #c는 가중치
    g[a][b]=c
    

for i in range(1,n+1):
    for j in range(1,n+1):
        print(g[i][j], end=' ')
    print()
