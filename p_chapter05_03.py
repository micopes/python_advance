# Chapter05-03
# 일급 함수(일급 객체)
# 클로저 심화
# '외부에서 호출된 함수의 변수 값', 상태(레퍼런스) 복사 후 저장 -> 후에 해당 상태로 접근(액세스 가능)

# Closure 사용
def closure_ex1():
    # Free variable(자유 변수)
    # 클로저 영역
    series = []
    def averager(v):
        series.append(v)
        print("inner >>> {} / {}".format(series, len(series)))
        return sum(series) / len(series)
    return averager

# 해당 scope에 접근하여 해당 상태로 접근 가능.
avg_closure1 = closure_ex1()

print(avg_closure1(10))
print(avg_closure1(30))
print(avg_closure1(50))
print(avg_closure1(70))

print()
print()

# function inspection
print(dir(avg_closure1))
print()
print(dir(avg_closure1.__code__))
print(avg_closure1.__code__.co_freevars) # 자유 변수를 갖고 있다.(series)
print(avg_closure1.__closure__[0].cell_contents) # 자유 변수가 담고 있는 내용을 전달한다.(series 리스트 내부의 값.)
print()

# 잘못된 클로저 사용의 예.
def closure_ex2():
    # Free variable
    cnt = 0
    total = 0

    def averager(v):
        cnt += 1
        total += v
        return total / cnt
    return averager

avg_closure2 = closure_ex2()
# print(avg_closure2(10)) # 예외 발생

def closure_ex3():
    # Free variable
    cnt = 0
    total = 0

    def averager(v):
        nonlocal cnt, total # 위의 cnt, total을 이용한다고 선언해야 한다.
        cnt += 1
        total += v
        return total / cnt
    return averager

avg_closure3 = closure_ex3()

print(avg_closure3(15))
print(avg_closure3(35))
print(avg_closure3(40))

# 전역변수, global을 사용하는 경우 유지보수가 어려울 수 있으므로, 이런 식으로 Closure를 사용하면 유용하다.