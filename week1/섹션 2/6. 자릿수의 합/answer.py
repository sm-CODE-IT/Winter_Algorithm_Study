def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum


n = int(input())
nums = list(map(int, input().split()))
res = 0
max = 0
for i in nums:
    temp = digit_sum(i)
    if (temp > max):
        max = temp
        res = i
print(res)
