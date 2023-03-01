#동전 분배하기


def DFS(L,s1,s2,s3):
    if L==n:
        m = max(s1,s2,s3)
        l = min(s1,s2,s3)
        if max-min<res:
            res = max-min
    else:
        DFS(L+1,s1+li[L],s2,s3)
        DFS(L+1,s1,s2+li[L],s3)
        DFS(L+1,s1,s2,s3+li[L])

    
if __name__=="_main_":
    li=list()
    n= int(input())
    res=2147000000
    for i in range(n):
        li.append(i)
    DFS(0,0,0,0)
#확인

#강의 설명
'''
상태 트리 -> A,B,C로 가지를 나눠서 (0,1,2) 동전을 합해주기 -> 내가 만든거랑 비슷
back을 할 때 주의-> 넣어줬던 코인 값을 취소해야함. 
'''

def DFS(L):
    global res
    if L == n:
        cha = max(money)-min(money)
        if cha<res:
            tmp=set() #중복허락x
            for x in money :
                tmp.add(x)
            if len(tmp)==3:
                res = cha
    else:
        for i in range(3):
            money[i]+=coin[L]
            DFS(L+1)
            money[i]-=coin[L] #for back

if __name__=="_main_":
    n=int(input())
    coin =list()
    money=[0]*3
    res = 2147000000
    for _ in range(n):
        coin.append(int(input()))
    DFS(0)

