# Chapter02-01
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등 -> 유지보수, 대형프로젝트에 적합

# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 파라미터 감소, 구성요소들이 객체로 관리된다. -> 유지보수, 대형 프로젝트에 적합

# 일반적인 코딩

# 차량 1
car_company = 'Ferrari'
car_detail_1 = [
    {'color' : 'White'},
    {'horsepower' : 400},
    {'price' : 8000}
]

# 차량 2
car_company = 'BMW'
car_detail_1 = [
    {'color' : 'Black'},
    {'horsepower' : 270},
    {'price' : 5000}
]

# 차량 3
car_company = 'AUDI'
car_detail_1 = [
    {'color' : 'Silver'},
    {'horsepower' : 300},
    {'price' : 6000}
]

# 리스트 구조
# 관리하기가 불편
# 인덱스 번호를 알아야 하므로, 인덱스 접근 시 실수 가능성, 삭제 불편
car_company_list = ['Ferrari', 'BMW', 'AUDI']
car_detail_list = [
    {'color' : 'White', 'horsepower' : 400, 'price' : 8000},
    {'color' : 'Black', 'horsepower' : 270, 'price' : 5000},
    {'color' : 'Silver', 'horsepower' : 300, 'price' : 6000}
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)

print()
print()


# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제(키는 중복을 허용하지 않는다.), 키 조회 예외 처리 필요.

car_dicts = [
    {'car_company': 'Ferrari', 'car_detail': {'color' : 'White', 'horsepower' : 400, 'price' : 8000}},
    {'car_company': 'BMW', 'car_detail': {'color' : 'Black', 'horsepower' : 270, 'price' : 5000}},
    {'car_company': 'AUDI', 'car_detail': {'color' : 'Silver', 'horsepower' : 300, 'price' : 6000}}
]

del car_dicts[1]
print(car_dicts)

print()
print()

# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용

# Car(object) 기본적으로 object 메소드를 상속받는 것이 default.
# Car(object) = Car() = Car 모두 같다.
class Car():
    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

car1 = Car('Ferrari', {'color' : 'White', 'horsepower' : 400, 'price' : 8000})
car2 = Car('BMW', {'color' : 'Black', 'horsepower' : 270, 'price' : 5000})
car3 = Car('AUDI', {'color' : 'Silver', 'horsepower' : 300, 'price' : 6000})

# __str__이 없는 경우에는 주소값이 출력되지만 클래스 내부에 __str__이 있는 경우 __str__을 이용해서 출력한다. -> 사용자 입장에서 출력(print)을 원할 시에 __str__을 사용하고
# 객체 상의 출력을 원하는 경우에는 __repr__을 사용한다.(eval 등 객체를 인식할 수 있는 경우) - 좀 더 엄밀한 경우 사툥(개발자 입장)

# __str__과 __repr__ 이 모두 있는 경우에는 __str__을 이용해서 출력하지만, 
# __str__이 없는 경우에는 __repr__을 이용해서 출력한다. 둘다
# 둘 다 없는 경우에는 주소 값을 출력한다.

print(car1)
print(car2)
print(car3)

# __dict__을 이용하면 객체의 세부 사항들을 확인할 수 있다.(딕셔너리 형태로.)

print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

print()
print()

# dir(객체)를 이용하면 객체가 사용할 수 있는 메타정보를 다 보여준다. ex) __dict__, __str__과 같은 것들
print(dir(car1))

# 리스트 선언 (__repr__ 을 이용해서 출력해준다.)
car_list = []

car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(car_list)

print()
print()

# 반복(__str__)
for x in car_list:
    print(x)
