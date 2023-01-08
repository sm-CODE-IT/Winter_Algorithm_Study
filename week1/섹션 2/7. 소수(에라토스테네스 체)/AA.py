# 소수 개수 구하기(에라토스테네스 체)

n = int(input())
cnt = [0] * (n + 1)
res = 0

for i in range(2, n + 1):
    if (cnt[i] == 0):
        res += 1
        for j in range(i + i, n + 1, i):
            if j % i == 0:
                cnt[j] = 1
print(res)
