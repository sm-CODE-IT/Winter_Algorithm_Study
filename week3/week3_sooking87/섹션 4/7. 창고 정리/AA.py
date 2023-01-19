l = int(input())
dummy = list(map(int, input().split()))
n = int(input())

for _ in range(n):
    highest = max(dummy)
    lowest = min(dummy)
    hIdx = dummy.index(highest)
    lIdx = dummy.index(lowest)
    dummy[hIdx] -= 1
    dummy[lIdx] += 1

print(max(dummy) - min(dummy))
