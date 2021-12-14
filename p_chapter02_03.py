class Car():
    '''
    Car class
    Author : Kang
    Date : 2021.12.14
    Description : Class, Static, Instance Method
    '''
    # 클래스 변수 (모든 인스턴스가 공유. Car1, Car2, Car3을 호출하여 총 3번 호출하게 되면 아래의 __init__이 3번 호출되므로 car_count가 3으로 출력된다.)
    price_per_raise = 1.2

    # 인스턴스 변수
    def __init__(self, company, details):
        self._company = company
        self._details = details

    # 인스턴스 메소드(self(객체의 고유한 속성 값을 사용)를 인자로 받는 것)
    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))
    
    def get_price(self):
        return "Before Car Price -> company : {}, price : {}".format(self._company, self._details.get('price'))

    def get_price_culc(self):
        return "After Car Price -> company : {}, price : {}".format(self._company, self._details.get('price') * Car.price_per_raise)

    # 클래스 메소드. 첫 인자로 cls - Car를 받는다. Car를 사용하는 대신에 cls를 사용하는 것.
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print("Please Enter 1 or More")
            return
        cls.price_per_raise = per
        print("Succeed! price increased.")

    # 스태틱 메소드는 어떤 인자도 받지 않는다 넣어도 되고. 자유롭게 사용하도록 만든 것인데. 꼭 필요하지는 않다는 의견도 있다.
    @staticmethod
    # inst는 그냥 적은것 aaa나 아무거나 해도 된다.
    def is_bmw(inst):
        if inst._company == 'BMW':
            return 'Ok! This car is {}'.format(inst._company)
        return 'Sorry. This car is not BMW.'

        


car1 = Car('Ferrari', {'color' : 'White', 'horsepower' : 400, 'price' : 8000})
car2 = Car('BMW', {'color' : 'Black', 'horsepower' : 270, 'price' : 5000})

# 전체 정보
car1.detail_info()
car2.detail_info()

# 가격 정보(직접 접근) -> 이렇게 하는 것은 좋지 못한 방식. Java나 C++에서 private을 사용하는 이유. 
# print(car1._details.get('price')) 
# print(car2._details.get('price')) 

# 가격 정보(인상 전)
print(car1.get_price())
print(car2.get_price())

# 가격 정보(인상 후)
# 아래의 방법으로 클래스 변수를 수정하는 것이 나쁜 방법은 아니나 로직을 추가할 수 없다.
# 클래스 메소드 미사용
Car.price_per_raise = 1.4

print(car1.get_price_culc())
print(car2.get_price_culc())

# 아래의 방식으로 클래스 메소드를 사용하게 되면 값 변경 뿐만아니라 로직 또한 추가할 수 있다.
# 클래스 메소드 사용
Car.raise_price(1.6)

print(car1.get_price_culc())
print(car2.get_price_culc())

# 스태틱 메소드 사용 클래스를 호출해도 되고 인스턴스를 호출해도 된다.
# 인스턴스로 호출
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
# 클래스로 호출
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))



