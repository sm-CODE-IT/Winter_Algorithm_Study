def count(capacity):
    cnt = 1  # DVD 개수
    sum = 0
    for x in minute:
        if (sum + x) > capacity:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt


n, m = map(int, input().split())
minute = list(map(int, input().split()))
min = sum(minute)

maxx = max(minute)
start = 1
end = min
res = 0
while start <= end:
    mid = (start + end) // 2
    if mid >= maxx and count(mid) <= m:
        res = mid
        end = mid - 1
    else:
        start = mid + 1
print(res)
