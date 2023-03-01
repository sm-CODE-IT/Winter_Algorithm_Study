#송아지 찾기

def DFS(h,c):
    global cnt
    if h==c:
        cnt+=1
    else:
        DFS(h+1,c)
        DFS(h-1,c)
        DFS(h+5,c)

if __name__=="_main_":
    n,m = map(int(), input().split())
    #현수의 위치가 송아지의 위치보다 앞에 있을 수도 있으므로 함부로 빼기를 하진 않는다.
    cnt = 0
    DFS(5,14)
    print(cnt)