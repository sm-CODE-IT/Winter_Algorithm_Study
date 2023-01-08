# N의 약수 중 K번째로 작은 수 출력

N, K = map(int, input().split())
'''
nums = []
for i in range(1, N + 1):
    if (N % i == 0):
        nums.append(i)

if (len(nums) <= K):
    print(-1)
else:
    print(nums[K - 1])
'''

cnt = 0
for i in range(1, N + 1):
    if N % i == 0:
        cnt += 1
    if cnt == K:
        print(i)
        break
# for 문이 정상 완료가 된다면 else 문 실행
else:
    print(-1)
