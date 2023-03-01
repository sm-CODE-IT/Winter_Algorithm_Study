# 합이 같은 부분집합
import sys

def DFS(L,sum): #L은 레벨.  a에 접근하는 인덱스 번호, sum은 누적값
    if sum>total//2:
        return
    if L == n:
        if sum==(total-sum):
            print("yes")
            sys.exit(0)
    else:
        DFS(L+1,sum+a[L]) #왼쪽 노드로 감 -> a[L]을 사용함
        DFS(L+1,sum)



if __name__ == "_main_":
    n=input()
    a=list(map(int,input().split()))
    total=sum(a)
    DFS(0,0)
    #같은 경우가 없을 경우는 따로 no 출력
    print("NO")

#시간 복잡도 줄이기
#sum의 값이 total/2보다 작거나 같을 것임. 절반을 넘어가면 트리의 밑 가닥을 갈 필요가 없음
#sum==total//2는 안돼. 총합이 홀수일 경우 두 부분집합의 합이 같을 수가 없음
