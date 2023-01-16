def getDivisor(num):
    divisorList = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisorList.append(i)
    return divisorList


t = input()
answer = ""
for i in range(len(t)):
    if t[i] >= '0' and t[i] <= '9':
        answer += t[i]

answer = int(answer)
print(answer)
print(len(getDivisor(answer)))
