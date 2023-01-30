n = list(map(str, input()))
operator = []
res = ""

# 연산자 우선순위
# ()
# *, /
# +, -
guide = {')': 0, '(': 0, '*': 2, '/': 2, '+': 1, '-': 1}
for i in n:
    if '0' <= i <= '9':
        res += i
    else:
        if i == '(':
            operator.append(i)
        elif i == '*' or i == '/':
            while operator and (operator[-1] == '*' or operator[-1] == '/'):
                res += operator.pop()
            operator.append(i)
        elif i == '+' or i == '-':
            while operator and (operator[-1] != '('):
                res += operator.pop()
            operator.append(i)
        elif i == ')':
            while operator and operator[-1] != '(':
                res += operator.pop()
            operator.pop()
while operator:
    res += operator.pop()
print(res)
