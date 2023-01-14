n, m, k=map(int, input().split())
num_list=list(map(int,input().split()))

num_list.sort()
num_list.reverse()

first=num_list[0]
second=num_list[1]
answer=0

while True:
    for i in range(k):
        if (m == 0): break
        answer+=first
        m-=1
    if(m==0): break
    answer+=second
    m-=1

print(answer)