n = int(input())
nums = list(map(int, input().split()))

maxSum = 0
maxIdx = 0
for i in range(len(nums)):
    sum = 0
    for j in range(len(str(nums[i]))):
        sum += int(str(nums[i])[j])

    if (sum > maxSum):
        maxSum = sum
        maxIdx = i
print(nums[maxIdx])
