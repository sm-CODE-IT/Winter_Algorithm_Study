n = int(input())
profile = []
for _ in range(n):
    height, weight = map(int, input().split())
    profile.append((height, weight))

profile.sort()
cnt = 0
for i in range(n):
    current = profile[i][1]
    canIn = True
    for j in range(i + 1, n):
        if current < profile[j][1]:
            canIn = False
    if canIn:
        cnt += 1

print(cnt)
