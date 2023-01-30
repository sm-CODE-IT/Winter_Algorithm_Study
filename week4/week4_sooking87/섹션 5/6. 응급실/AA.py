# n, m = map(int, input().split())
# people = list(map(int, input().split()))
# num = people[m]
# cnt = 0

# while people:
#     standard = people.pop(0)
#     max = standard
#     for i in range(len(people)):
#         if max < people[i]:
#             max = people[i]

#     if standard != max:
#         people.append(standard)
#         people.remove(max)
#     cnt += 1

#     if max == num:
#         print(cnt)
#         break

# ? 위험도가 같은 경우는 인덱스로 어떻게 구분을 하지?
from collections import deque
n, m = map(int, input().split())
people = [(pos, val)
          for pos, val in enumerate(list(map(int, input().split())))]
# enumerate: 인덱스와 원소를 동시에 접근할 수 있다.
people = deque(people)
cnt = 0

while True:
    cur = people.popleft()  # cur은 튜플 형태임
    # any 함수를 통해서 max를 구할 수 있음
    if any(cur[1] < x[1] for x in people):
        people.append(cur)
    else:
        cnt += 1
        if cur[0] == m:
            break
print(cnt)
