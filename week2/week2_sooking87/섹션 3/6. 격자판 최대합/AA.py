n = int(input())
board = []

for i in range(n):
    row = list(map(int, input().split()))
    board.append(row)

sum = []
for row in range(n):
    temp1 = 0
    temp2 = 0
    for col in range(n):
        temp1 += board[row][col]
        temp2 += board[col][row]
    sum.append(temp1)
    sum.append(temp2)

temp = 0
for i in range(n):
    temp += board[i][i]
sum.append(temp)

print(max(sum))
