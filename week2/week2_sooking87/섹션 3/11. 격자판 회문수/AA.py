def getRotate(nums):
    if nums == nums[::-1]:
        return True
    else:
        return False


grid = [list(map(int, input().split())) for _ in range(7)]

cnt = 0
for start in range(3):
    for j in range(7):
        # 행 검사
        temp = grid[j][start: start + 5]
        if getRotate(temp):
            cnt += 1
        # 열 검사 -> 슬라이스로 검사를 할 수 없으므로 맨앞-맨뒤 이런식으로 반복문을 돌리면서 직접 비교를 한다. 5개를 가지고 비교를 하는 것이므로 2번만 비교를 하면 됨.
        for k in range(2):
            if grid[start + k][j] != grid[start + 5 - k - 1][j]:
                break
        else:
            cnt += 1
print(cnt)
