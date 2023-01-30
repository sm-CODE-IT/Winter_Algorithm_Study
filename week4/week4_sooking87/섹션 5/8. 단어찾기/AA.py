n = int(input())
write = []
poem = []

for _ in range(n):
    write.append(input())

for _ in range(n - 1):
    poem.append(input())

for i in range(n):
    if write[i] in poem:
        continue
    else:
        print(write[i])
        break
