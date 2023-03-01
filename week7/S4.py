#순열 구하기

def DFS(L,res):
    if L==m:
        for i in range(len(res)):
            print(res[i],end=" ")
    else:
        for i in range(n):
            res[i]=1
            DFS(L+1,res)


if __name__ =="_main_":
    n,m=map(int,input().split())
    li=[]
    res=[0]*n
    for i in range(n):
        li.append(i)
    DFS(0,res)

    #문제점 -> 리스트를 따로 만들어서 보관할 순 없을까
    #일단 그냥 check 리스트 만듦


#강의 설명

'''
중복이 되지 않도록 체크리스트에 체크해가면서 
ch라는 리스트를 만들어서 0 -> 4개


1을 선택했으면 ch[1] == 1
다음 가지를 뻗었을 때 ch==0일때만 뻗을 수 있고 1이면 중복이라서 안돼

D(2)에서 끝난 다음 D(1)으로 back한다. 근데 이때 체크되어 있던 ch[2]==1 -> 0으로 바꿔줘야 한다.
백을 할 때는 다른 가닥에서 사용해야하므로 0을 풀어주는 과정을 거친다.

'''
def DFS(L):
    global cnt
    if L ==m:
        for j in range(L):
            print(res[j],end=" ")
            print()
            cnt+=1
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1
                res[L]=i #작업 후 곧 호출 일어남
                DFS(L+1)
                ch[i]=0  #호출이 일어난 후 되돌아 오는 지점


if __name__=="_main_":
    n,m = map(int,input().split())
    res = [0]*n 
    ch= [0]*(n+1)  #체크리스트 01234 -> 0은 안쓰는듯. 그래서 for i in range(1,n+1)
    cnt=0   #갯수
    DFS(0)
    print(cnt)

#꼭 다시 보기 -> ch는 i로, res는 L로.


