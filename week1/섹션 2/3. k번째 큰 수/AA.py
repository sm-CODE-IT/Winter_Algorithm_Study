n, k = map(int, input().split())
nums = list(map(int, input().split()))
res = set()  # 이렇게 set을 해두면 res에 어떤 숫자든 한개만 들어가게 된다. 중복 제거

for i in range(n):
    for j in range(i + 1, n):
        for m in range(j + 1, n):
            res.add(nums[i] + nums[j] + nums[m])

res = list(res)
res.sort(reverse=True)  # 내림차순
print(res[k - 1])
