# Chapter05-02
# 일급 함수(일급 객체)
# 클로저 기초

# 파이썬 변수 범위(scope)

# EX1)
def func_v1(a):
    print(a)
    print(b)

# func_v1(10)

# EX2)
b = 20
def func_v2(a):
    print(a)
    print(b)

func_v2(10)

# EX3) - 에러
# c = 30

# def func_v3(a):
#     print(a)
#     print(c) # 'scope 안'에 같은 이름이 있는 경우는 뒤에 나오더라도 local 변수로 인식한다. 근데 로컬 변수가 먼저 선언되지 않기 때문에 에러가 난다.
#     c = 40
# func_v3(10)

# Closure(클로저) - 스코프가 닫혀도 값을 '기억'한다.
# 서버 프로그래밍 -> 동시성(Concurrency) 제어 -> 메모리 공간에 여러 자원이 접근 -> 교착 상태(Deadlock)
# 메모리를 공유하지 않고 메시지 전달로 처리하기 위한 -> Erlang
# 클로저는 공유하되 변경되지 않는(Immutable, Read Only) 구조를 적극적으로 사용 -> 함수형 프로그래밍
# 클로저는 불변자료구조 및 atom, STM -> 멀티스레드(Coroutine을 통해 단일 스레드에서도 병행성 가능) 프로그래밍에 강점

a = 100

print(a + 100)
print(a + 1000)

# 결과 누적(함수 사용)
print(sum(range(1, 51)))
print(sum(range(51, 101)))

# 클래스 이용
class Averager():
    def __init__(self):
        self._series = []

    # __call__을 이용하면 클래스를 함수처럼 이용할 수 있다.
    def __call__(self, v):
        self._series.append(v)
        print("inner >> {} / {}".format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)

# 인스턴스 생성
averager_cls = Averager()

# 누적 - 해당 스코프(여기서는 클래스)의 내용이 함수는 종료되었지만, 값(여기서는 리스트)을 기억하고 있다.
print(averager_cls(10)) # [10]
print(averager_cls(30)) # [10, 30]
print(averager_cls(50)) # [10, 30, 50]
print(averager_cls(70)) # [10, 30, 50, 70]
print(averager_cls(193)) # [10, 30, 50, 70, 193]