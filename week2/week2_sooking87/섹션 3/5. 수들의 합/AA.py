n, sumRes = map(int, input().split())
nums = list(map(int, input().split()))
lt = 0
rt = 1
sum = nums[0]
cnt = 0

while True:
    if sum < sumRes:
        if rt < n:
            sum += nums[rt]
            rt += 1
        else:
            break
    elif sum == sumRes:
        cnt += 1
        sum -= nums[lt]
        lt += 1
    else:
        sum -= nums[lt]
        lt += 1

print(cnt)
