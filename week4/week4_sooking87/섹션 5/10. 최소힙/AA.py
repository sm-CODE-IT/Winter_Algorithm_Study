import heapq

heap = []
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(heap) == 0:
            print(-1)
        else:
            res = heapq.heappop(heap)
            print(res)
    else:
        heapq.heappush(heap, n)
