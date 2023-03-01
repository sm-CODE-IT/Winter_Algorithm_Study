#바둑이 승차

result=0
def DFS(L,sum):
    if L==m:
        if sum <=n and sum>result:
            result=sum
    else:
        DFS(L+1,sum+li[L])
        DFS(L+1,sum)


if __name__=="_main_":
    n,m=map(int,input().split())
    li = []
    for i in range(m):
        li.append(int(input()))
    DFS(0,0)


#강의 설명
def DFS(L,sum,tsum): #바둑이 몸무게 리스트의 인덱스 번호
    global result #전역변수이다 알려줘야 함.

    if sum+(total-tsum)<result: #현재 판단한(부분집합에 넣는다 안넣는다.) = tsum
        #total - tsum -> 현재 여기까지 판단한 바둑이의값을 뺀 것이므로 앞으로 적용해야할 바둑이의 몸무게(아직 판단x)
        #sum+(total-tsum) -> 지금까지 만든 부분집합 + 앞으로 남은 바둑이의 몸무게
        

        return

    if sum>c:
        return #and로 연결하면 안되려나
    #sum>c하면 time 초과. 더 커트를 해야함. -> cut-edge


    if L == n:
        if sum>result: #여기서 로컬변수인데 참조중(result 초기화 안 한 상태인데)
             result = sum #->값을 다시 할당했으므로 전역변수 => 로컬변수가 됨

    else:
        DFS(L+1,sum+a[L],tsum+a[L])
        DFS(L+1,sum,tsum+a[L])


if __name__ =="_main_":
     c,n = map(int,input().split())
     a=[0]*n #바둑이 각각의 몸무게를 저장
     result = -2147000000
     for i in range(n):
         a[i]= int(input())
     total=sum(a)
     DFS(0,0,0)