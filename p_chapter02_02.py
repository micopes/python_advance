class Car():
    '''
    Car class
    Author : Kang
    Date : 2021.12.14
    '''
    # 클래스 변수 (모든 인스턴스가 공유. Car1, Car2, Car3을 호출하여 총 3번 호출하게 되면 아래의 __init__이 3번 호출되므로 car_count가 3으로 출력된다.)
    car_count = 0

    # 인스턴스 변수
    def __init__(self, company, details):
        self._company = company
        self._details = details
        Car.car_count += 1

    # 인스턴스 메소드
    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    def __del__(self):
        Car.car_count -= 1

    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

# Self 의미
car1 = Car('Ferrari', {'color' : 'White', 'horsepower' : 400, 'price' : 8000})
car2 = Car('BMW', {'color' : 'Black', 'horsepower' : 270, 'price' : 5000})
car3 = Car('AUDI', {'color' : 'Silver', 'horsepower' : 300, 'price' : 6000})

# ID 확인 (주소값)
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company)
print(car1 is car2)

# dir & __dict__ 확인
print(dir(car1))
print(dir(car1))

print()
print()

print(car1.__dict__)
print(car2.__dict__)

# Doctoring - 주석을 적어놓은 것. 사용법 및 수정한 사람 등 확인 가능.
print(Car.__doc__)
print()

# 실행 - car1.detail_info()의 경우에는 자동으로 self 매개변수가 전달된다. - 밑의 것과 서로 같은 결과를 출력한다.
car1.detail_info()
Car.detail_info(car1)
car2.detail_info()
Car.detail_info(car2)

# 비교 클래스의 자체의 주소를 나타내는 것이므로 같다.
print(car1.__class__, car2.__class__)
print(id(car1.__class__) == id(car2.__class__) == id(car3.__class__))

# 에러 - self가 없기 때문에.
# Car.detail_info()

# 클래스 변수. 모든 인스턴스에서 공유, _를 앞에 붙이지 않은 것은 암묵적으로 클래스 변수라고 안다. 인스턴스 변수는 _를 앞에 붙여주자.
print(car1.car_count)
print(car2.car_count)

# __dict__를 사용하면 클래스 변수는 나오지 않고 인스턴스 변수, 메소드만 출력된다.
print(car1.__dict__)
print(car2.__dict__)

# dir을 사용하는 경우에는 인스턴스 변수, 메소드, 클래스 변수까지 모두 보여준다.
print(dir(car1))

# 접근 인스턴스를 이용해서 접근해도 되고, 클래스 이름으로 바로 접근(추천)할 수도 있다.
print(car1.car_count)
print(Car.car_count)

# del 메소드가 호출이 되는 경우 count를 감소
del car2
# 삭제 확인
print(Car.car_count)

# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 변수 검색 후 -> 상우(클래스 변수, 부모 클래스 변수)를 찾는다.)
