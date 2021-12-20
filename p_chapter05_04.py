# Chapter05-03
# 일급 함수(일급 객체)
# 클로저 심화
# '외부에서 호출된 함수의 변수 값', 상태(레퍼런스) 복사 후 저장 -> 후에 해당 상태로 접근(액세스 가능)
# Chapter05-04
# 일급 함수(일급 객체)

# 클로저
# 데코레이터(Decorator) @

# 장점
# 1. 중복 제거, 코드 간결, 공통 함수 작성
# 2. 로깅, 프레임워크, 유효성 체크 ... 등 가능 -> 공통 기능
# 3. 조합해서 사용 용이

# 단점
# 1. 가독성 감소
# 2. 특정 기능에 한정된 함수는 -> 단일 함수로 작성하는 것이 유리
# 3. 디버깅 불편

# 데코레이터 실습
import time

# 어떤 함수든 공통적으로 실행 시간을 뽑을 수 있다 -> 다른 함수를 장식해줄 수 있다 : 데코레이터.
def perf_clock(func):
    def perf_clocked(*args):
        # 함수 시작 시간
        st = time.perf_counter()
        # 함수 실행
        result  = func(*args)
        # 함수 종료 시간
        et = time.perf_counter() - st
        # 실행 함수명
        name = func.__name__
        # 함수 매개변수
        arg_str = ', '.join(repr(arg) for arg in args)
        # 결과 출력
        print('[%0.5fs] %s(%s) -> %r' % (et, name, arg_str, result))
        return result
    return perf_clocked


def time_func(seconds):
    time.sleep(seconds)

def sum_func(*numbers):
    return sum(numbers)

# 데코레이터 미사용 - 내가 만든 함수 이용해서 새로운 선언이 필요하다.
none_deco1 = perf_clock(time_func)
none_deco2 = perf_clock(sum_func)

print(none_deco1, none_deco1.__code__.co_freevars)
print(none_deco2, none_deco2.__code__.co_freevars)

print('-' * 40, 'Called None Decorator -> time_func')
print()
none_deco1(1.5)
print('-' * 40, 'Called None Decorator -> sum_func')
print()
none_deco2(100, 200, 300, 400, 500)

print()
print()

# 데코레이터 사용 - 내가 만든 함수 위에 @표시를 통해 데코레이터 추가해주고 내가 만든 함수를 그냥 사용하면 된다.
def perf_clock(func):
    def perf_clocked(*args):
        # 함수 시작 시간
        st = time.perf_counter()
        # 함수 실행
        result  = func(*args)
        # 함수 종료 시간
        et = time.perf_counter() - st
        # 실행 함수명
        name = func.__name__
        # 함수 매개변수
        arg_str = ', '.join(repr(arg) for arg in args)
        # 결과 출력
        print('[%0.5fs] %s(%s) -> %r' % (et, name, arg_str, result))
        return result
    return perf_clocked

@perf_clock # 추가!
def time_func(seconds):
    time.sleep(seconds)

@perf_clock # 추가!
def sum_func(*numbers):
    return sum(numbers)

print('-' * 40, 'Called Decorator -> time_func')
print()
time_func(1.5)
print('-' * 40, 'Called Decorator -> sum_func')
print()
sum_func(100, 200, 300, 400, 500)