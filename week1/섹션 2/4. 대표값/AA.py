n = int(input())
scores = list(map(int, input().split()))
sum = 0

for i in range(n):
    sum += scores[i]

# avg = round(sum / n)
'''
파이썬에서의 round 함수는 5까지 버림을 하고 6부터 올림을 해주는 방식이다. 그래서 4.5라면 4가 나오게 된다. 

그래서 0.5를 더하고 int 형으로 바꾸어 버리면 소수점이 5부터는 올림을 해주고 4까지는 버림이 된다. 
'''
avg = sum / n
avg += 0.5
avg = int(avg)

minDiff = 100
minNum = 0
for i in range(len(scores)):
    temp = abs(avg - scores[i])
    if (temp < minDiff):
        minDiff = temp
        score = scores[i]
        minNum = i + 1
    elif (temp == minDiff):
        if (score < scores[i]):
            score = scores[i]
            minNum = i + 1

print(avg, minNum)
