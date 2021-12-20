# Chapter06-05
# Futures, 병렬성
# 비동기 작업 실행

# 지연 시간(Block) CPU 및 리소스 낭비 방지 -> (File)Network I/O 관련 작업 -> 동시성 활용 권장(제어권을 다른 데 넘겨서 다른 작업 수행하기 위해서.)
# 비동기 작업에 적합한 프로그램일 경우 압도적으로 성능 향상


# import threading
# import multiprocessing
# 위의 두 가지를 사용하는데에 어려움이 많았는데 futures로 두 가지를 래핑했다.

# futures : 비동기 실행을 위한 API를 고수준으로 작성 -> 사용하기 쉽도록 개선
# concurrent.Futures
# 1. 멀티스레딩/멀티프로세싱 API 통일 -> 매우 사용하기 쉬움
# 2. 실행 중인 작업 취소, 완료 여부 체크, 타임 아웃 옵션, 콜백 추가, 동기화 코드 매우 쉽게 작성 -> Promise 개념(비동기 작업의 결과를 나타내는 객체)

# 2가지 패턴 실습
# concurrent.futures map
# concurrent.futures wait, as_completed
# -> convoy effect, 실패 등을 세부적으로 관리할 수 있어야 한다.

# GIL(Global Interpreter Lock) : 두 개 이상의 스레드가 동시에 실행될 때 하나의 자원을 액세스하는 경우 -> 문제점을 방지하기 위해 GIL이 실행된다.
# GIL이 실행되면 : 리소스 전체에 Lock이 걸린다. -> Context Switching 비용이 발생하므로 멀티스레드를 사용하는 경우 오히려 싱글스레드보다 효율이 떨어지는 경우가 발생할 수 있다.

# GIL : 멀티프로세싱 사용, CPython을 이용해서 GIL을 우회.

import os, time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait, as_completed

WORK_LIST = [1000, 10000, 100000, 1000000] # 여기 작업을 [work1, work2, work3, work4] 와 같이 해서 작업을 수행할 수도 있다.

# 동시성 합계 계산 메인 함수
# 누적 합계 함수(제너레이터)

def sum_generator(n):
    return sum(n for n in range(1, n+1))

def main():
    # Worker Count
    worker = min(10, len(WORK_LIST)) # 지정하지 않으면 OS에서 알아서 지정해준다.
    
    # 시작 시간
    start_tm = time.time()
    # Futures
    futures_list = []
    
    # 결과 건수
    # ProcessPoolExecutor/ThreadPoolExecutor
    with ThreadPoolExecutor() as executor:
        for work in WORK_LIST:
            # future 반환(미래의 할 일을 반환). 실행되는 것은 아님
            future = executor.submit(sum_generator, work)
            # 스케줄링
            futures_list.append(future)
            # 스케줄링 확인
            print("Scheduled for {} : {}".format(work, future))

        '''
        # wait 결과 출력
        result = wait(futures_list, timeout = 1) # 1초를 넘는 작업은 wait!
        # 성공
        print("Completed Tasks : " + str(result.done))
        # 실패
        print("Pending ones after waiting for 1 second" + str(result.not_done))
        # 결과 값 출력
        print([future.result() for future in result.done])
        '''

        # as_completed 결과 출력
        for future in as_completed(futures_list):
            result = future.result()
            done = future.done()
            cancelled = future.cancelled

            # future 결과 확인
            print("Future Result : {}, Done : {}".format(result, done))
            print("Future Cancelled : {}".format(cancelled))


    # 종료 시간
    end_tm = time.time() - start_tm
    # 출력 포맷
    msg = '\n Result -> {} Time : {:.2f}s'
    # 최종 결과 출력
    # print(msg.format(list(result), end_tm))
    # print(msg.format(end_tm))


# 실행 시작점 명시 : 이것 없으면 멀티프로세싱 작업이 안된다.
if __name__ == '__main__':
    main()


# 결론
# wait : timeout을 줄 수 있다. 
# as_completed : 먼저 처리된 것을 바로 처리할 수 있다.
# -> 작업이 실행되고 바로 다른 작업을 수행하기 위해서 주로 사용.