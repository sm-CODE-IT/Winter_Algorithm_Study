def isRightOneLine(line):
    line.sort()
    for i in range(1, 10):
        if i != line[i - 1]:
            return False
    return True


sudoku = []

for i in range(9):
    row = list(map(int, input().split()))
    sudoku.append(row)

# 행 검사
isRight = True
for i in range(9):
    # 그냥 temp = sudoku[i]를 하게 되면 같은 주소 공간을 가리키게 된다. 그래서 list라는 새로운 객체를 만들어주어야 한다.
    temp = list(sudoku[i])
    if not isRightOneLine(temp):
        isRight = False

if isRight:
    # 열 검사
    for i in range(9):
        temp = []
        for j in range(9):
            temp.append(sudoku[j][i])
        if not isRightOneLine(temp):
            isRight = False

if isRight:
    # 9칸 검사
    for i in range(9):
        if i % 3 == 0:
            temp1 = []
            temp2 = []
            temp3 = []
        for j in range(9):
            if 0 <= j <= 2:
                temp1.append(sudoku[i][j])
            elif 3 <= j <= 5:
                temp2.append(sudoku[i][j])
            else:
                temp3.append(sudoku[i][j])

        if i % 3 == 2:
            if not isRightOneLine(temp1):
                if not isRightOneLine(temp2):
                    if not isRightOneLine(temp3):
                        isRight = False
if isRight:
    print("YES")
else:
    print("NO")
