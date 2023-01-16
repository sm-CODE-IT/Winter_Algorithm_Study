n1 = int(input())
firstList = list(map(int, input().split()))
n2 = int(input())
secondList = list(map(int, input().split()))

answer = firstList + secondList
answer.sort()

for i in answer:
    print(i, end=' ')
