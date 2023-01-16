n = int(input())
map = [list(map(int, input().split())) for _ in range(n)]
map.insert(0, [0]*n)
map.append([0]*n)

for x in map:
    x.insert(0, 0)
    x.append(0)

cnt = 0
# 상하좌우 비교를 할 때 이런식으로 한다.
x = [0, -1, 0, 1]
y = [-1, 0, 1, 0]
for row in range(1, n + 1):
    for col in range(1, n + 1):
        max = map[row][col]
        # all : 모두가 참일 때
        if all(max > map[row + y[k]][col + x[k]] for k in range(4)):
            cnt += 1

print(cnt)
