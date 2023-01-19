n = int(input())
# 회의가 끝나는 기준으로 정렬하면 됨
meeting = []
for _ in range(n):
    start, end = map(int, input().split())
    meeting.append((start, end))
# 회의가 끝나는 시간을 우선적으로 정렬 -> 그 다음 회의 시작 시간을 정렬
meeting.sort(key=lambda x: (x[1], x[0]))
endTime = 0
cnt = 0
for s, e in meeting:
    if s >= endTime:
        endTime = e
        cnt += 1
print(cnt)
