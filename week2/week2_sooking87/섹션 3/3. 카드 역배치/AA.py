def getReverse(switchCards):
    temp = []
    for i in range(len(switchCards)-1, -1, -1):
        temp.append(switchCards[i])
    return temp


cards = [i for i in range(1, 21)]

for i in range(10):
    a, b = map(int, input().split())
    switchCards = cards[a - 1: b]
    switchCards = getReverse(switchCards)
    cards[a - 1: b] = switchCards

for i in cards:
    print(i, end=' ')
