# Chapter06-01
# 병행성(Concurrency)
# Generator(제너레이터): 이터레이터를 리턴(생성)하는 함수, yield를 사용하며 메모리 적재 방식에서 이터레이터와 차이가 있다.
# Iterator(이터레이터): 반복 가능한 객체

# 단순히 yield를 쓰냐 안쓰냐의 차이도 있지만 
# 가장 큰 차이점은 이터레이터는 모든 동작을 완료한 후 결과를 한번에 메모리 적재
# 제너레이터는 각각의 yield에서 한번 실행 시킨 후 대기 상태에 들어가 결과를 반환, 이후 다음 코드를 진행하여 또다시 yield를 만날 경우 대기 상태에 들어가 결과를 반환하는 방식입니다.

# 파이썬 반복 가능한 타입
# collections, text file, List, Dict, Set, Tuple, unpacking, *args, iterable하게 구현된(한) 클래스 등 : iterable

t = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print(dir(t)) # __iter__
# 반복 가능한 이유 ? -> iter(x) 함수 호출할 수 있다.
for c in t:
    pass
    # print(c)

# 반복문의 내부적 원리는 다음과 같다.
# while
w = iter(t)

# print(next(w)) # 다음에 나올 순서를 기억하고 있다.
while True:
    try:
        print(next(w))
    except StopIteration:
        break
print()

# 반복형 확인
from collections import abc

# print(dir(t)) # __iter__가 있는지
print(hasattr(t, '__iter__')) # __iter__가 있는지
print(isinstance(t, abc.Iterable)) # Iterable을 상속받았는지

print()
print()

# next 패턴
class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(" ")

    def __next__(self):
        print("Called __next__")
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration("Stopped Iteration.")
        self._idx += 1
        return word

    def __repr__(self):
        return "WordSplit(%s)" % self._text

# 클래스도 iterable하게 사용할 수 있다.
wi = WordSplitter('Do today what you could do tomorrow.')

print(wi)
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))

# Generator 패턴
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 양 증가. 증가 후 메모리 사용량 증가 -> 제너레이터 사용 권장
# 2. 단위 실행 가능한 코루틴(Coroutine) 구현과 연동
# 3. 작은 메모리 조각 사용

class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(' ')
    
    def __iter__(self):
        for word in self._text:
            yield word # 제네레이터
        return

    def __repr__(self):
        return "WordSplitGenerator(%s)" % self._text

wg = WordSplitGenerator('Do today what you could do tomorrow.')

wt = iter(wg)

print(wt, wg)
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))

# next를 이용하는 경우에는 idx를 따로 구현해야 하며,
# generator의 yield keyword를 사용하는 경우에는 내부적으로 다음에 반환될 값의 위치 정보를 기억하고 있다.