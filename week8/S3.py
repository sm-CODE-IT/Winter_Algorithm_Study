#양팔저울
'''
오른쪽에 두는 것 -> +
왼쪽에 두는 것 -> -
의문 -> back을 해야할까?
n2와 num의 비교 방법 -> how efficient
'''
def DFS(sum):
    n2=set()
    if sum>m:
        return
    elif sum<m:
        n2.append(sum)
    else:
        for i in range(n):
            DFS(sum+li[n])
            DFS(sum-li[n]) 

if __name__=="_main_":
    n=int(input())
    li=list(map(int,input().split()))
    m=0
    for i in range(n):
        m+=li[i]
    num=list()
    for i in range(n):
        num.append(i+1)

#강의설명
'''
총합 13가지 중에서 가능한 가지 수 (11)을 뺀 값을 출력
양팔저울의 왼쪽에 두기 vs 오른쪽에 두기(-) vs 아예 추를 두지 않기

'''

if __name__=="_main_":
