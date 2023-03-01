#중복 순열

'''
D(0)에서 가지가 뻗어나갈 때 for문 안에서 리스트 res[L]=i를 호출해야함
res는 m크기

if L==m이면 res를 출력해주기.(종착점)
출력만하고 호출이 없으면 끝남 -> back



'''
import sys
input = sys.stdin.readline #readline 시 대량의 입력을 읽을 때 효율=> 입력 속도 빨라짐
#문자열을 읽을 때는 줄바꿈 기호까지 읽으므로
s = input().rstrip()

def DFS(L):
    if L ==m:
        #res 출력
        for j in range(m):
            print(res[j],end=" ")
        print()
        cnt+=1
    else:
        for i in range(1,n+1):
            res[L]=i
            DFS(L+1) #n,m=3,2일 때 세 가닥으로 뻗는 것을 표현

if __name__ == "_main_":
    n,m = map(int,input().split())
    res = [0]*m
    cnt=0
    DFS(0)
    print(cnt)