n = int(input())
reverse = list(map(int, input().split()))
res = [0 for i in range(n)]
for i in range(n):
    for j in range(n):
        if (reverse[i] == 0 and res[j] == 0):
            res[j] = i + 1
            break
        elif res[j] == 0:
            reverse[i] -= 1
for x in res:
    print(x, end=' ')
