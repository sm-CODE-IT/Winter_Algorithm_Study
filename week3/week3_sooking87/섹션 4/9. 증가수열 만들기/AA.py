from collections import deque

n = int(input())
nums = list(map(int, input().split()))
nums = deque(nums)
cnt = 0
res = ""
delNum = 0
while nums:
    if delNum < min(nums[0], nums[-1]):
        if nums[0] > nums[-1]:
            res += "R"
            delNum = nums.pop()
        else:
            res += "L"
            delNum = nums.popleft()
    else:
        if max(nums[0], nums[-1]) == nums[0]:
            res += "L"
            delNum = nums.popleft()
        else:
            res += "R"
            delNum = nums.pop()
    cnt += 1

    if (delNum > nums[0]) and (delNum > nums[-1]):
        break
print(cnt)
print(res)
