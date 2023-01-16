def getMoved(n, arrow, space, list):
    moved = []
    if arrow == 0:
        for i in range(len(list)):
            moved.append(list[(i + space) % n])
    if arrow == 1:
        haveToMove = n - space
        for i in range(len(list)):
            moved.append(list[(i + haveToMove) % n])
    return moved


def getSum(ground):
    n = len(ground)
    start = 0
    end = n
    sum = 0
    for row in range((n // 2) + 1):
        for col in range(start, end):
            sum += ground[row][col]
        start += 1
        end -= 1
    start -= 1
    end += 1
    for row in range((n // 2) + 1, n):
        start -= 1
        end += 1
        for col in range(start, end):
            sum += ground[row][col]
    return sum


# 0이면 왼쪽, 1이면 오른쪽
n = int(input())
ground = []
for i in range(n):
    temp = list(map(int, input().split()))
    ground.append(temp)

commandCnt = int(input())
for i in range(commandCnt):
    row, arrow, space = map(int, input().split())
    copy = ground[row - 1]
    movedList = getMoved(n, arrow, space, copy)
    ground[row - 1] = movedList

sum = getSum(ground)
print(sum)
