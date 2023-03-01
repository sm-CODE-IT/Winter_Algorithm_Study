#동전 바꾸기
'''
상태트리 -> 동전 종류별로 넣/말로 가지 나누기
'''

def DFS(L,sum):
    global cnt
    if sum>n:
        return
    if sum==n:
        cnt+=1
    else:
        for k in range(m):
            if num[k]>0:
                DFS(L+1,sum+coin[k])
                num[k]-=1

if __name__=="_main_":
    n= int(input())
    m=int(input())
    coin=list()
    num=list()
    cnt=0
    for _ in range(m):
        i,j = map(int,input().split())
        coin.append(i)
        num.append(j)
    DFS(0,0)
    print(cnt)


#강의 설명
'''
DFS(L,sum)-> sum이 동전 합
상태트리 -> 5원짜리 동전을 0개, 1개, 2개, 3개 사용한다.
 10원 -> 0, 1, 2 개 사용
 1원 -> 0,1,2,3,4,5개 사용



'''

def DFS(L,sum):
    global cnt
    if sum>T:
        return
    if L==k:
        if sum==T:
            cnt+=1
    else:
        for i in range(cn[L]+1): #cn[L]+1을 해야 0~L번까지 돈다
            DFS(L+1,sum+(cv[L]*i)) #*i

if __name__=="_main_":
    T=int(input())
    k = int(input())
    cv = list()
    cn = list()
    for i in range(k):
        a,b = map(int,input().split())
        cv.append(a)
        cn.append(b)
    cnt=0
    DFS(0,0)
    print(cnt)
    