# Chapter07-01
# Async I/O
# 비동기 I/O  Coroutine 작업
# Generator -> 반복적인 객체 Return 사용
# Non-blocking 비동기 처리

# Blocking I/O : 호출된 함수가 자신의 작업이 완료될때까지 제어권을 가지고 있음. 타 함수는 대기
# Nonblocking I/O : 호출된 함수가(서브루틴) return 후 호출한 함수(메인 루틴)에 제어권 전달 -> 타 함수는 일 지속

# 스레드 단점 : 디버깅, 자원 접근 시 레이스 컨디션(경쟁 상태), 데드락(Dead Lock) -> 고려 후 코딩
# 코루틴 장점 : 하나의 루틴만 실행 -> 락 관리 필요 X -> 제어 권으로 실행
# 코루틴 제약 : 사용 함수가 비동기로 구현이 되어 있거나, 직접 비동기로 구현해야 한다.

import asyncio
import timeit
from urllib.request import urlopen # Block 함수임. asyncio로 구현하는 효과가 크지 않다. ->  각각 Block I/O지만, 따로 구현해서 상관없도록 구현
from concurrent.futures import ThreadPoolExecutor
import threading

# 실행 시작 시간
start = timeit.default_timer()

# 서비스 방향이 비슷한 사이트로 실습 권장(예 : 게시판성 커뮤니티)
urls = ['http://daum.net', 'http://naver.com', 'http://mlbpark.donga.com', 'https://tistory.com', 'https://wemakeprice.com']

async def fetch(url, executor):
    # 스레드명 출력
    print("Thread Name : ", threading.current_thread().getName(), 'Start', url)
    # 실행 - 결과를 보면 종료되는 순서는 다를 수 있다(비동기이기 때문에 제대로 나온 것.)
    res = await loop.run_in_executor(executor, urlopen, url) # urlopen이 block 함수인데 여기서 nonblock으로 만들어서 수행
    print("Thread Name : ", threading.current_thread().getName(), 'Done', url)

    # 결과 반환
    return res.read()[0:5]

async def main():
    # 스레드 풀 생성
    executor = ThreadPoolExecutor(max_workers = 10)
    
    # future 객체 모아서 gather에서 실행
    futures = [
        asyncio.ensure_future(fetch(url, executor)) for url in urls # url하나 당 하나의 스레드
    ]

    # 결과 취합 - await는 yield 대신 사용
    rst = await asyncio.gather(*futures)

    print()
    print("Result : ", rst)


if __name__ == '__main__':
    # 루프 초기화
    loop = asyncio.get_event_loop()
    # 작업 완료까지 대기
    loop.run_until_complete(main())
    # 수행 시간 계산
    duration = timeit.default_timer() - start
    # 총 실행 시간
    print("Total Running Time : ", duration)


