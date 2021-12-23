# `with`
Airflow를 공부하다보니 
```
with DAG() as dag:
```
이런 방식으로 시작되는 코드가 존재한다.

정확히 `with`이 어떤 기능을 하는 구문인지 알아보자.


`with`은 파이썬 2.5에서 도입된 기능으로 context manager에 의해서 실행되는 `__enter__()`과 `__exit__()`을 정의하여, `with` 구문 body 의 앞부분과 뒷부분에 실행되는 코드를 대신할 수 있다.
`with` 구문을 이용하면 `try/finally`을 대신하여 더 간편하고 쉽게 사용할 수 있다.
<br>

## `try/finally`
다음과 같이 `try/finally`를 사용한 코드를 보자
```
set things up
try:
    do something
finally:
    tear things down
```
1. `자원을 획득`
2. `자원을 사용`
3. `자원을 반납`
의 과정으로 진행되며, 코드가 제대로 사용되지 않고 끝나더라도 자원은 반납된다.

위의 과정을 `__enter__()`, `__exit__()`를 사용하여 클래스로 구성하면 유지 보수 측면에서 유리할 것이다.

## `with` 문 사용

```
class Hello:
    def __enter__(self):
        # 사용할 자원을 가져오거나 만든다(핸들러 등)
        print('enter...')
        return self # 반환값이 있어야 VARIABLE를 블록내에서 사용할 수 있다
        
    def sayHello(self, name):
        # 자원을 사용한다. ex) 인사한다
        print('hello ' + name)

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 마지막 처리를 한다(자원 반납 등)
        print('exit...')
```

```
with Hello() as h:
    h.sayHello('A')
    h.sayHello('B')
```

#### 결과
```
enter...
hello A
hello B
exit...
```

필요 이상으로 오래 자원, 권한을 가지고 있거나 여기저기 넘기면서 불필요한 객체에게 넘겨서는 안되며, 각 객체들은 단일 책임을 지고 설계된 라이프사이클에 따라 움직여야 한다.

`with`을 사용하면 효율적으로 객체의 라이프사이클(생성 >> 사용 >> 소멸)을 설계할 수 있다.

이런 유지보수 측면과 자원, 권한 관리의 효율성 측면에서 `with` statement는 유용하게 사용할 수 있다.


<br><br>

#### Reference
- https://docs.python.org/3/reference/datamodel.html#context-managers
- https://cjh5414.github.io/python-with/
- https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=wideeyed&logNo=221653260516
- http://effbot.org/zone/python-with-statement.htm
