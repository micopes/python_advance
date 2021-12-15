# Chapter04-04
# 시퀀스형
# 해시 테이블(Hash Table) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> Key 중복 허용 X, Set -> 중복 허용 X
# Dict 및 Set 심화 - 읽기 전용, 최적화

# Immutable Dict
from types import MappingProxyType
from typing import Mapping

d = {'key1': 'value1'}

# Read only
d_frozen = MappingProxyType(d)

print(d, id(d))
print(d_frozen, id(d_frozen))

# 수정 가능
d['key2'] = 'value2'

# 수정 불가 - Error
# d_frozen['key2'] = 'value2'

print()

# 집합 자료형
s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3}
s4 = {} # 이 때는 딕셔너리로 선언이 된다.
print(type(s4))

# 수정 불가 set
s5 = frozenset(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])

s1.add('Melon')
print(s1)

# 추가 불가
# s5.add('Melon')

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))

# 선언 최적화
# 바이트 코드 -> 파이썬 인터프리터 실행
# dis를 통해 바이트 코드 생성 순서를 확인할 수 있다.
from dis import dis

print("-------")
print(dis('{10}'))
print("-------")
print(dis('set([10])')) # 이렇게 set()을 통해서 집합을 구성하는 것이 step이 더 많다. 조금 더 느릴 수 있다.

# 지능형 집합(Comprehending Set)
from unicodedata import name

print("------")
print({name(chr(i), '') for i in range(256)})









