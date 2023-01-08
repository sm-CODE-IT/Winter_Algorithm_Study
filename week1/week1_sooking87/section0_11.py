def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def isPrime(x):
    flag = 1
    for i in range(2, x):
        if (x % i == 0):
            flag = 0

    if flag == 1:
        return True
    else:
        return False


a = 10
b = 2
nums = [12, 13, 7, 9, 19, 2, 3]

addNum = add(a, b)
subNum = sub(a, b)
mulNum = mul(a, b)
divNum = div(a, b)

print(addNum)
print(subNum)
print(mulNum)
print(divNum)

for i in nums:
    if isPrime(i):
        print(i, end=' ')

# * temp
