# Chapter04-02
# 시퀀스형
# 컨테이너(Container : 서로 다른 자료형을 담을 수 있는 자료형([list, tuple, collections.deque]))
# 플랫(Flat : 한 종류의 자료형만 담을 수 있는 자료형[str, bytes, bytearray, array.array, memoryview]) - 한 종류이므로 연산 속도가 빠르다
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)
# 리스트 및 튜플 고급

# Tuple Advanced
# Unpacking
# ex) b, a = a, b

print(divmod(100, 9))
print(divmod(*(100, 9))) # Tuple Unpacking
print(*(divmod(100, 9))) # Tuple Unpacking

print()

x, y, *rest = range(10)
print(x, y, rest)
x, y, *rest = range(2)
print(x, y, rest)
x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest)

print()

# Mutable(가변) vs Immutable(불변)
l = (15, 20, 25)
m = [15, 20, 25]

print(l, id(l))
print(m, id(m))

l = l*2
m = m*2

print(l, id(l))
print(m, id(m))

l *= 2
m *= 2

# List형은 Tuple형과 달리 id값이 변하지 않은 것을 확인할 수 있다.
print(l, id(l))
print(m, id(m))

print()

# sort vs sorted
# reverse, key = len, key = str.lower, key = func...

# sorted : 정렬 후 새로운 객체 반환(원본 수정 X), inplace = False라고 생각하면 된다.

f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'coconut']
print('sorted - ', sorted(f_list))
print('sorted - ', sorted(f_list, reverse = True))
print('sorted - ', sorted(f_list, key = len)) # 길이순 정렬
print('sorted - ', sorted(f_list, key = lambda x : x[-1], reverse = True)) # 끝 글자를 기준으로

print('sorted - ', f_list)

# sort : 정렬 후 객체 직접 변경, 반환값 None, inplace = True
print('sort - ', f_list.sort(), f_list)
print('sort - ', f_list.sort(reverse = True), f_list)
print('sort - ', f_list.sort(key = len), f_list)
print('sort - ', f_list.sort(key = lambda x : x[-1]), f_list)
print('sort - ', f_list.sort(key = lambda x : x[-1], reverse = True), f_list)

# List vs Array
# List : 융통성, 다양한 자료형, 범용적 사용
# Array : 숫자 기반, 리스트와 거의 호환.