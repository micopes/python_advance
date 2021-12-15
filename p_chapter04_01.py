# Chapter04-01
# 시퀀스형
# 컨테이너(Container : 서로 다른 자료형을 담을 수 있는 자료형([list, tuple, collections.deque]))
# 플랫(Flat : 한 종류의 자료형만 담을 수 있는 자료형[str, bytes, bytearray, array.array, memoryview]) - 한 종류이므로 연산 속도가 빠르다
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes

# 리스트 및 튜플 고급

# 지능형 리스트(Comprehending Lists)
chars = '!@#$%^&*()_+'
code_list1 = []

for s in chars:
    # 유니코드 리스트
    code_list1.append(ord(s))

print(code_list1)

# Comprehending Lists - for문보다 속도가 약간 우세하다고 한다.
code_list2 = [ord(s) for s in chars]

print(code_list2)

# Comprehending Lists + Map, Filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]
code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))

# 전체 출력
print(code_list1)
print(code_list2)
print(code_list3)
print(code_list4)
print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])

print()
print()

# Generator 생성
# Generator란? : sequence result를 만들어내고 *local state를 유지하고, 다음번에 반환할 값의 위치를 정확하게 가지고 있다. - powerful iterator - iterator: 작은 메모리 조각으로 값을 이끌어 낼 수 있다.
import array

# Generator : 한 번에 한 개의 항목을 생성(메모리 유지 X)
tuple_g = (ord(s) for s in chars)
array_g = array.array('I', (ord(s) for s in chars))

print(type(tuple_g))
print(next(tuple_g))
print(array_g)
print(type(array_g))
print(array_g.tolist())

print()
print()

# Generator 예제
print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)))

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)):
    print(s)

print()
print()

# 리스트 주의할 점
marks1 = [['~'] * 3 for _ in range(4)]
marks2 = [['~'] * 3] * 4

print(marks1)
print(marks2)

print()

# 수정 [['~', 'X', '~'], ['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]
marks1[0][1] = 'X'
print(marks1)

# 의도하지 않은 결과값 수정 [['~', 'X', '~'], ['~', 'X', '~'], ['~', 'X', '~'], ['~', 'X', '~']]
# id 값이 원하는대로 개별적으로 구성이 되지 않음
marks2[0][1] = 'X'
print(marks2)

# 확인
print([id(i) for i in marks1]) # [140703129798720, 140703138535360, 140703129798528, 140703129798464] - 다 다른 것으로 구성 deep copy
print([id(i) for i in marks2]) # [140703152992000, 140703152992000, 140703152992000, 140703152992000] - 다 같은 id를 복사한 것이 된다. shallow copy

