num, m = map(int, input().split())
num = list(map(int, str(num)))
stack = []

for x in num:
    # x기준 앞에 있는 애들이 x보다 작을 경우
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1

    stack.append(x)

if m > 0:
    stack = stack[:-m]

res = ''.join(map(str, stack))
print(res)
