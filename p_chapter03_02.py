# Chapter03-02
# Special Method(Magic Method)
# 파이썬의 핵심 : 시퀀스(Sequence), 반복(Iterator), 함수(Function), 클래스(Class)
# 클래스 안에 정의할 수 있는 특별한(Built-in) 메소드
# Built in -> 내부적으로 어떻게 이미 만들어진 것을 사용해서 이뤄지는지

# 클래스 예제 2

class Vector():
    def __init__(self, *args):
        '''
        Create a vector, example : v = Vector(5, 10)
        '''
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        '''
        Return the vector informations
        '''
        return "Vector(%r, %r)" % (self._x, self._y)

    def __add__(self, other):
        '''
        Return the vector addition of self and other
        '''
        return Vector(self._x + other._x, self._y + other._y)
    
    def __mul__(self, y):
        '''
        Return the vector multiple of self and other
        '''
        return Vector(self._x * y._x, self._y * y._y)

    def __bool__(self):
        return bool(max(self._x, self._y))

# 각 인스턴스 메소드 내의 주석을 얻기 위해서, 매
print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)
print(Vector.__mul__.__doc__)

# 매직 메소드 출력 - 메소드가 개발하는 사람의 목적에 맞게 구현이 되면 그것이 매직 메소드.
v1 = Vector(5, 7)
v2 = Vector(23, 17)
v3 = Vector()

print(v1, v2, v3)
print(v1 + v2)
print(v1 * v2)

print(bool(v1))
print(bool(v2))
print(bool(v3)) # 0이므로 False가 출력