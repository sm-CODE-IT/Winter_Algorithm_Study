# from collections import deque

# temp = input()
# essential = list(map(str, temp))
# essential.append('F') # * 지대 어거지긴 하다,,,
# n = int(input())

# for i in range(1, n + 1):
#     cnt = 0
#     ess = essential[cnt]
#     timeTable = input()
#     for j in timeTable:
#         if ess == j:
#             cnt += 1
#             ess = essential[cnt]
#     if cnt == len(essential) - 1:
#         print("#%d YES" % i)
#     else:
#         print("#%d NO" % i)

# ? essential을 popleft하게 되면 남는게 없는데,,, copy를 해서 사용할 수는 없을까?
# ? 왜 계속 인덱스 에러가 뜨는 거지? -> 첫 번째 입력값에서 timeTable은 돌아가고, essential안에 있는 수업들은 다 찾았으니까

# ? 필수 수업중에 마지막 수업을 못찾더라도 이미 pop된 상태이므로 essential 자체에는 남아있는 수업이 없다. 그래서 if not essential 조건문에 걸리게 되는데 이거는 어떻게 해결할까? -> 찾으면 pop을 시키는? 식으로?
# ? 아니면 같은 수업을 발견하면 cnt += 1 하는 식으로? 그리고 그 cnt == len(essential)이게 되면 break

from collections import deque
essential = input()
n = int(input())
for i in range(1, n + 1):
    plan = input()
    dq = deque(essential)
    for x in plan:
        if x in dq:
            if x != dq.popleft():  # 필수과목이 계획에 있긴 한데 그게 순서에 맞지 않으면
                print("#%d NO" % (i))
                break
    else:
        if len(dq) == 0:
            print("#%d YES" % (i))
        else:
            print("else")
            print("#%d NO" % (i))
