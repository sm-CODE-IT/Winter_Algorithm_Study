from collections import deque


def bfs(x, y):
    # 이동할 네 가지 방향 정의
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # deque 생성
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 그래프 내에서 벗어나면 안됨
            if nx < 0 or nx >= row or ny < 0 or ny >= col:
                continue
            # 0 이면 이동 불가
            if graph[nx][ny] == 0:
                continue
            # 1 이면 이동 가능
            if graph[nx][ny] == 1:
                # 이동 횟수를 위해서 전에 (x, y)가 몇 번째 이동한 것인지를 체크
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                print(graph)
    return graph[row-1][col-1]


row, col = map(int, input().split())
graph = []

for _ in range(row):
    graph.append(list(map(int, input())))
print(graph)
# (0, 0)부터 탐색
print(bfs(0, 0))
