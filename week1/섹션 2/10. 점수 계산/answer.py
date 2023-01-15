n = int(input())
score = list(map(int, input().split()))
cnt = 0  # 연속되어서 맞추었는지 아닌지 확인
sum = 0
for i in range(n):
    if (score[i] == 1):
        cnt += 1
        sum += cnt
    else:
        cnt = 0

print(sum)
