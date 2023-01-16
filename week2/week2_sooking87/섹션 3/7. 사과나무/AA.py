n = int(input())
farm = []
for i in range(n):
    temp = list(map(int, input().split()))
    farm.append(temp)

start = n // 2
end = start + 1
sum = 0
for row in range((n // 2) + 1):
    for col in range(start, end):
        sum += farm[row][col]
    start -= 1
    end += 1

start += 1
end -= 1
for row in range((n // 2) + 1, n):
    start += 1
    end -= 1
    for col in range(start, end):
        sum += farm[row][col]

print(sum)
