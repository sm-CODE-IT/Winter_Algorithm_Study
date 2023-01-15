def reverse(x):
    num = 0
    k = 1
    for i in range(len(str(x))):
        num += k * int(str(x)[i])
        k *= 10
    return num


def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    else:
        return True


n = int(input())
nums = list(map(int, input().split()))
for i in nums:
    revNum = reverse(i)
    if (isPrime(revNum)):
        print(revNum, end=' ')
