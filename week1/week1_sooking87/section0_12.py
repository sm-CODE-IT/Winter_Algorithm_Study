# 람다 함수

def plus_one(x):
    return x + 1


print(plus_one(1))


def plus_two(x): return x + 2


print(plus_two(1))

# 람다 함수 -> 익명의 함수로 사용하는 경우가 많다. 이럴 때 유용하다.

a = [1, 2, 3]
print(list(map(lambda x: x + 2, a)))
