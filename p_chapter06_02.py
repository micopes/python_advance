# Chapter06-02
# 병행성(Concurrency) : 한 컴퓨터(CPU, 스레드)가 여러 일을 동시에 수행 - 어디까지 작업을 수행했는지 알고 있어야 한다. 그런 개념으로 사용하는 것이 Closure 같은 것들
# -> 단일 프로그램 안에서 여러 일을 쉽게 해결(독립적으로 느끼게 해준다.)
# 병렬성(Parallelism) : 여러 컴퓨터가 여러 일을 동시에 수행
# -> 속도. 각자 맡은 일을 수행함으로써 전체적인 속도가 빨라진다.

# Generator EX1

def generator_ex1():
    print('Start')
    yield 'A Point' # return의 역할도 한다.
    print('Continue')
    yield 'B Point'
    print('End')

temp = iter(generator_ex1())

# print(temp)
print(next(temp)) # next(temp)시 A Point -> A Point를 기억했다가
print(next(temp)) # next(temp)시 B Point가 수행된다.

for v in generator_ex1():
    pass

# Generator EX2
temp2 = [x * 3 for x in generator_ex1()]
temp3 = (x * 3 for x in generator_ex1()) # Generator

print(temp2)
print(temp3)

for i in temp3:
    print(i)

print()
print()

# Generator EX3(중요 함수)
# count, takewhile, filterfalse, accumulator, chaijn, product, groupby ...

import itertools

gen1 = itertools.count(1, 2.5) # itertools.count(시작, 증가단위), but, 끝이 없다.

print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))

# 조건

gen2 = itertools.takewhile(lambda n : n < 1000, itertools.count(1, 2.5)) # 끝 지점을 만든다. takewhile은 count와 함께 사용 가능.

for v in gen2:
    pass 
    # print(v)

# 필터 반대 - 필터와 반대되는 것이 나온다.daf
gen3 = itertools.filterfalse(lambda n : n < 3, [1, 2, 3, 4, 5])

for v in gen3:
    print(v)

# 누적 합계
gen4 = itertools.accumulate([x for x in range(1, 101)])

for v in gen4:
    pass
    # print(v)

# 연결 1
gen5 = itertools.chain("ABCDE", range(1, 11, 2))
print(list(gen5))

# 연결2
gen6 = itertools.chain(enumerate('ABCDE'))
print(list(gen6))

# 개별
gen7 = itertools.product("ABCDE")
print(list(gen7))

# 연산 - 중복 포함 경우의 수
gen8 = itertools.product("ABCDE", repeat = 2)
print(list(gen8))

# 그룹화
gen9 = itertools.groupby("AAABBCCCCDDEEE")
# print(list(gen9))
for chr, group in gen9:
    print(chr, ' : ', list(group))