n, m, k=map(int, input().split())
num_list=list(map(int, input().split()))

num_list.sort()
num_list.reverse()

answer=0
K=k

while m>0:
    if K>0:
        answer+=num_list[0]
        print(num_list[0])
        K-=1
        m-=1

    if K==0:
        answer+=num_list[1]
        print(num_list[1])
        m -= 1
        K=k

print(answer)
