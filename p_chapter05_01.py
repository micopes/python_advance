# Chapter05-01
# 일급 함수(일급 객체)
# 파이썬 함수 특징 -> 이 것들이 가능하다면 함수형 프로그래밍 가능.
# 1. 런타임 초기화
# 2. 함수를 변수에다 할당 가능
# 3. 함수를 다른 함수의 인자로 전달 가능
# 4. 함수를 결과로 반환 가능(return)

# 함수 객체

def factorial(n):
    '''
    Factorial Function -> n : int
    '''
    if n == 1:
        return 1
    return n*factorial(n-1)

class A:
    pass

print(factorial(5))
print(factorial.__doc__)
print(type(factorial), type(A))
print(set(sorted(dir(factorial))) - set(sorted(dir(A)))) # 함수만 갖고 있는 것들. {'__globals__', '__name__', '__annotations__', '__defaults__', '__kwdefaults__', '__code__', '__call__', '__closure__', '__get__', '__qualname__'}
print(factorial.__name__)
print(factorial.__code__)

print()
print()

# 변수 할당
var_func = factorial

print(var_func) # 할당된 것을 확인할 수 있다.
print(var_func(10))
print(list(map(var_func, range(1, 11))))

# 함수를 인자로 전달 및 함수로 결과 반환 가능
# -> 고위 함수(Higher-order function)
# map, filter, reduce

# 람다 함수를 filter 함수의 인자로 전달한 것.
print(list(map(var_func, filter(lambda x : x % 2, range(1, 6)))))
print([var_func(i) for i in range(1, 6) if i % 2])

print()
print()

# reduce 
from functools import reduce
from operator import add

print(reduce(add, range(1, 11))) # 뒤의 것을 하나하나씩 감소시켜가면서 누적시켜서 add를 수행한다.
print(sum(range(1, 11)))

# 익명 함수(lambda)
# 가급적 주석을 꼭 작성해라.
# 가급적 함수를 이용. 일반 함수로 리팩토링을 권장함.

print(reduce(lambda x, t : x + t, range(1, 11)))

print()
print()

# Callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인.
# 호출 가능 확인
print(callable(str), callable(list), callable(var_func), callable(factorial), callable(3.14))

# partial 사용법 : 인수 고정 -> 콜백 함수 사용
from operator import mul
from functools import partial

print(mul(10, 10))

# 인수 고정 (5를 고정)
five = partial(mul, 5)

# 고정된 인수 2개 (5, 6)이 고정이므로 30이 나온다.
six = partial(five, 6)

print(five(10))
print(six())
print([five(i) for i in range(1, 10)]) # 구구단
print(list(map(five, range(1, 10))))