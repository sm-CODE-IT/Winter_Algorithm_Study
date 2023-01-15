t = int(input())
for i in range(t):
    n, s, e, k = map(int, input().split())
    nums = list(map(int, input().split()))
    temp = nums[s - 1: e]
    temp.sort()
    print("#%d %d" % (i + 1, temp[k - 1]))
