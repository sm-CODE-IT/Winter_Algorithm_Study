# 동전 교환
#15에서 1,2,5를 빼는 방식
def DFS(L,t,cnt):
    global result
    if t<0: # 더 많은 수를 뺀경우 cut
        return
    if t==0:
        if result>cnt:
            result=cnt
    else:
        for i in range(n):
            DFS(L+1,t-li[i],cnt+1)


if __name__ =="_main_":
    n=int(input())
    li = list(map(int,input().split()))
    total = int(input())
    result=2147000000
    DFS(0,total,0)
    print(result)



#강의 설명
'''
동전의 종류만큼 가지 뻗기
근데 나처럼 빼는 방식이 아닌 더하는 방식
D(L)-> L이 동전의 개수

깊이가 얕으면서 15를 만드는 경우의 L 값 출력

모든 레벨마다 동전의 개수만큼 가지 뻗기

'''

def DFS(L,sum):
    global res
    #time limit 발생 -> cut edge 필요.
    if L>res: #어차피 res값이 3인데 L이 4,5인 값들을 찾을 필요가 없다. res값이 갱신되지 않으니까.
        return
    if sum>m:
        return
    if sum == m:
        if L<res: #값이 할당되어 지역변수가 되었는데 참조 중 -> 에러 발생. 전역변수라고 선언 필요.
            res = L
    else:
        for i in range(n):
            DFS(L+1,sum+a[i]) # 동전의 종류만큼 가지를 뻗어야 하므로.


if __name__=="_main_":
    n=int(input())
    a= list(map(int,input().split()))
    m=int(input()) #m을 만들어야 한다
    res = 2147000000 #최소가 발견되면 바꿔야 한다.
    a.sort(reverse=True) #15원을 만들때 1원 ->15번 가지, 하지만 5원은 가지를 3번
    #sum이 m보다 커지면 return해서 가지 종료시켜야 함,
    #가지고 있는 res값보다 더 깊은 레벨로 들어갈 필요가 없음 -> cut
    #예를 들어 15원을 만드는데 5원으로는 3, 1원으로는 15번 -> 15번을 탐색할 필요가 없다. 어차피 res = 3
    #따라서 내림차순을 활용하는 것이 효율적 -> 안해도 ㄱㅊ
    DFS(0,0)
    print(res)
