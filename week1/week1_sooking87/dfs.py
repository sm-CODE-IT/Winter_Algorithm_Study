from collections import deque


def dfs(graph, start_node):
    # 기본은 항상 두개의 리스트를 별도로 관리해주는 것
    need_visited, visited = list(), list()

    # 시작 노드를 시정하기
    need_visited.append(start_node)

    while need_visited:
        # 그 중에서 가장 마지막 데이터를 추출 (스택 구조의 활용)
        node = need_visited.pop()
        if node not in visited:
            visited.append(node)
            # extend는 리스트 끝에 원소를 넣게 된다.
            # 인접 노드들을 방문 예정 리스트에 추가
            need_visited.extend(graph[node])

    return visited


def dfs2(graph, start_node):
    visited2 = []
    need_visited2 = deque()

    need_visited2.append(start_node)

    while need_visited2:
        node = need_visited2.pop()

        if node not in visited2:
            visited2.append(node)
            need_visited2.extend(graph[node])

    return visited2


def bfs(graph, start_node):
    need_visited3, visited3 = [], []
    need_visited3.append(start_node)

    while need_visited3:
        node = need_visited3[0]
        del need_visited3[0]

        if node not in visited3:
            visited3.append(node)
            need_visited3.extend(graph[node])

    return visited3


graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

print(dfs(graph, 'A'))
print(bfs(graph, 'A'))
