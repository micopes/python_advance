# Chapter06-02
# 병행성(Concurrency) : 한 컴퓨터(CPU, 스레드)가 여러 일을 동시에 수행 - 어디까지 작업을 수행했는지 알고 있어야 한다. 그런 개념으로 사용하는 것이 Closure 같은 것들
# -> 단일 프로그램 안에서 여러 일을 쉽게 해결(독립적으로 느끼게 해준다.)
# 병렬성(Parallelism) : 여러 컴퓨터가 여러 일을 동시에 수행
# -> 속도. 각자 맡은 일을 수행함으로써 전체적인 속도가 빨라진다.
# 코루틴(Coroutine)

# 코루틴 : 단일(싱글) 스레드, 스택을 기반으로 동작하는 비동기 작업
# 스레드 : OS에서 관리. CPU 코어에서 실시간, 시분할 비동기 작업 -> 멀티 스레드
# yield, send : 메인 <-> 서브
# 코루틴 제어, 상태, 양방향 전송

# 서브 루틴 : 메인 루틴 호출 -> 서브 루틴에서 수행(흐름 제어)
# 코루틴 : 루틴 실행 중 중지 -> 동시성 프로그래밍
# -> 스레드에 비해 오버헤드 감소(단일 스레드에서 진행하기 때문.)
# 스레드 : 싱글 스레드 -> 멀티 스레드 -> 복잡. 공유되는 자원때문에 교착상태나 Context Switching 비용이 생기며, 자원 소비 가능성 증가.

# Python 3.7이상에서는 def -> async, yield -> await로 사용할 수 있다.
# 함수인지 코루틴인지 명확하지 않을 수 있기 때문에. 이렇게 명시적으로 작성할 수 있다.

# 코루틴 EX1

# 서브 루틴
def coroutine1():
    print('>>> coroutine started.')
    i = yield
    print('>>> coroutine received : {}'.format(i))

# 메인 루틴 - 호출하는 곳.
# 제너레이터 선언
cr1 = coroutine1()

print(cr1, type(cr1))
'''
# yield 지점까지 서브 루틴 수행
next(cr1) # print('>>> coroutine started.')이 호출되고 yield에서 멈춤.

# 기본 전달 값 None
# 값 전송
cr1.send(100) # send라는 명령어를 이용해서 메인루틴과 서브루틴에서 서로 데이터 교환 가능.
'''

'''
# 잘못된 사용
cr2 = coroutine1()

cr2.send(100) # yield까지 도달하지 못한 상태로 send를 보내게 되면 에러.
'''

# 코루틴 EX2
# GEN_CREATED : 처음 대기 상태
# GEN_RUNNING : 실행 상태
# GEN_SUSPENDED : Yield 대기 상태 <= 이 지점이 중요!
# GEN_CLOSED : 실행 완료 상태

def coroutine2(x):
    print(">>> coroutine started : {}".format(x))
    y = yield x
    print(">>> coroutine received : {}".format(y))
    z = yield x + y
    print(">>> coroutine received : {}".format(z))

cr3 = coroutine2(10)

# 현재 generator의 상태를 확인할 수 있다.
from inspect import getgeneratorstate 

print(getgeneratorstate(cr3))
print(next(cr3))
print(getgeneratorstate(cr3))
print(cr3.send(100)) # *메인 루틴에서 100을 넘기고 서브 루틴으로부터 110을 받음*
# print(getgeneratorstate(cr3))
# cr3.send(200)

print()
print()

def generator1():
    for x in "AB":
        yield x
    for y in range(1, 4):
        yield y

t1 = generator1()

print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
# print(next(t1)) # StopIteration

t2 = generator1()
print(list(t2)) # 이렇게 바로 리스트로 받을 수도 있다.


# 위의 generator1와 같지만
# "yield from"을 사용할 수 있다.
def generator2():
    yield from "AB"
    yield from range(1, 4)

t3 = generator2()

print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))

