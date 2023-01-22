#행과 열의 크기 입력받기
n, m=map(int, input().split())

#2차원 배열로 행렬 입력받기
mylist=[]
for i in range(n):
    mylist.append(list(map(int,input().split())))

#각 행에 대해 최솟값을 판별 후 저장 
minlist=[]

for i in range(n): #i=0,1,2
    min = 100
    print(i)
    for j in range(m): #j=0,1,2
        if min>mylist[i][j]:
            min=mylist[i][j]
    minlist.append(min)

#print(minlist)


#모든 행에 대한 최솟값들 중 최댓값을 구해 출력
max=0
for i in range(n):
    if max<minlist[i]:
        max=minlist[i]

print(max)


