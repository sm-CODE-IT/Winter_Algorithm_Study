n, m = map(int, input().split())
res = [0 for i in range(n + m + 1)]
# res = [0] * (n + m + 3)

for i in range(1, n + 1):
    for j in range(1, m + 1):
        temp = i + j
        res[temp] += 1

max = 0
for i in range(len(res)):
    if (max < res[i]):
        max = res[i]

for i in range(len(res)):
    if (max == res[i]):
        print(i, end=' ')
