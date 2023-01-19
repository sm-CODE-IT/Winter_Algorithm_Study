n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
start = 0
end = n - 1

while start <= end:
    mid = (end + start) // 2
    if nums[mid] == m:
        print(mid + 1)
        break
    elif nums[mid] < m:
        start = mid + 1
    elif nums[mid] > m:
        end = mid - 1
