n = list(map(str, input()))
nums = []
for i in n:
    if not i.isdecimal():
        n2 = nums.pop()
        n1 = nums.pop()
        if i == '+':
            nums.append(n1 + n2)
        elif i == '-':
            nums.append(n1 - n2)
        elif i == '*':
            nums.append(n1 * n2)
        elif i == '/':
            nums.append(n1 / n2)
    else:
        nums.append(int(i))
print(nums.pop())
