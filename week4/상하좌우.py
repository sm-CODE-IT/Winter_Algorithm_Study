n=int(input())
dirs=list(map(str, input().split()))
x=1
y=1

for dir in dirs:
    if dir=='U':
        if y>1:
            y-=1
    if dir=='D':
        if y<n:
            y+=1
    if dir=='R':
        if x<n:
            x+=1
    if dir=='L':
        if x>1:
            x-=1

print(y,x)
