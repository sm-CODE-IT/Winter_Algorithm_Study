n, m, k=map(int, input().split())
num_list=list(map(int,input().split()))

num_list.sort()
num_list.reverse()

first=num_list[0]
second=num_list[1]
answer=0

firstcount=int(m/(k+1)*k+m%(k+1))
secondcount=m-firstcount

answer+=(firstcount*first)
answer+=(secondcount*second)
print(answer)