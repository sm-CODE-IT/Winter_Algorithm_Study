n = list(map(str, input()))
temp = []
cnt = 0
raser = 0

for i in range(len(n)):
    if n[i] == '(':
        temp.append(n[i])
    else:
        temp.pop()
        if n[i - 1] == '(':
            cnt += len(temp)
        else:
            cnt += 1
print(cnt)
