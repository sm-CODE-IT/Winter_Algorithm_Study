n = int(input())
ox = list(map(int, input().split()))
score = 0
isContinue = 1

for i in ox:
    if (i == 1) and (isContinue >= 1):
        score += isContinue
        isContinue += 1
    elif (i == 0):
        isContinue = 1
        continue
print(score)
