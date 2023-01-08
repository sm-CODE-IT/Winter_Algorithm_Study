from collections import deque


def DFS(start_node):
    visited[start_node] = True
    print(start_node, end=" ")

    for i in range(len(graph[start_node])):
        # 그래프에 존재하고, 방문하지 않은 경우
        if graph[start_node][i] == 1 and not visited[i]:
            DFS(i)


def BFS(start_node):
    queue = deque([start_node])
    visited[start_node] = True
    while queue:
        v = queue.popleft()
        if not visited[v]:
            print(v, end=" ")
            visited[v] = True
            for i in range(len(graph[v])):
                if graph[start_node][i] == 1 and not visited[i]:
                    queue.append(i)


n, m, v = map(int, input().split())

# 전역변수 graph -> 인접 리스트
graph = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    node1, node2 = map(int, input().split())
    graph[node1][node2] = graph[node2][node1] = 1

# 방문 여부
visited = [False] * (n + 1)
DFS(v)
print()

visited = [False] * (n + 1)
bfsList = BFS(v)
