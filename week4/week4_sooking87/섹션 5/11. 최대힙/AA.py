import heapq

maxHeap = []
while True:
    n = int(input())
    if n == -1:
        break

    if n == 0:
        if len(maxHeap) == 0:
            print(-1)
        else:
            res = heapq.heappop(maxHeap)[1]
            print(res)
    else:
        heapq.heappush(maxHeap, (-n, n))
