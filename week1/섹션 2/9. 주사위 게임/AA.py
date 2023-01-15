n = int(input())
money = []

for i in range(n):
    tempMoney = 0
    dice = list(map(int, input().split()))
    dice.sort()
    setDice = set(dice)
    lenSet = len(setDice)
    if (lenSet == 1):
        tempMoney = 10000 + dice[0] * 1000
    elif (lenSet == 2):
        tempMoney = 1000
        # 같은 눈 2개인 경우 같은 눈 찾기
        if (dice[0] == dice[1]):
            tempMoney += dice[0] * 100
        else:
            tempMoney += dice[2] * 100
    else:
        tempMoney = dice[2] * 100
    money.append(tempMoney)

money.sort()
print(money[n - 1])
