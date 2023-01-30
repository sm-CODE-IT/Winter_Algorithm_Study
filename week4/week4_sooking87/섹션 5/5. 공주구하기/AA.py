n, k = map(int, input().split())
prince = [i for i in range(1, n + 1)]
count = 1
while len(prince) != 1:
    if count == k:
        prince.pop(0)
        count = 1
    else:
        temp = prince.pop(0)
        prince.append(temp)
        count += 1
print(prince.pop())
