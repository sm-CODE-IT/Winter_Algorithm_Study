# k: 랜선의 개수, n: 필요한 랜선의 개수
# 이분 검색의 경우 결정 알고리즘에서 사용이 된다. 답이 특정 범위내에 있는 것을 알 수 있는 경우.

# 랜선이 있을 때, n 개를 맞추면서 동시에 최대로 자를 수 있는 랜선의 길이는 몇이냐는 문제
def count(lenLine):
    cnt = 0
    for x in line:
        cnt += (x // lenLine)
    return cnt


k, n = map(int, input().split())
# 답 범위가 1 ~ 802까지 가능은 하다. 일단 이렇게 범위를 잡는다. (1 + 802) // 2로 했을 때, 그 길이가 최대로 잡을 수 있는 랜선 길이인지를 이분 검색을 통해서 확인을 한다.
line = []
for _ in range(k):
    line.append(int(input()))

start = 1
end = max(line)
res = 0

while start <= end:
    mid = (start + end) // 2
    if count(mid) >= n:
        res = mid
        start = mid + 1
    elif count(mid) < n:
        end = mid - 1
print(res)
