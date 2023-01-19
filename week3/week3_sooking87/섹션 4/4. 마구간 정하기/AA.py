def count(distance):
    cnt = 1
    pos = room[0]
    for i in range(1, n):
        if room[i] - pos >= distance:
            cnt += 1
            pos = room[i]
    return cnt


n, c = map(int, input().split())
room = []
for _ in range(n):
    room.append(int(input()))
room.sort()

start = 1
end = max(room)
res = 0

while start <= end:
    mid = (start + end) // 2
    if count(mid) >= c:
        res = mid
        start = mid + 1
    else:
        end = mid - 1
print(res)
