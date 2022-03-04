"""
    timeit 

    함수를 문자열 형태로 만들어 인자로 넘겨주면
    해당 함수의 실행에 걸리는 시간을 반환한다.

    timeit("함수", number=해당 함수의 시행횟수)

    https://docs.python.org/ko/3/library/timeit.html
"""

import timeit as t

print(t.timeit("[]", number=10000000))
# [] 리스트 선언 1000만번 시행 시 걸리는 시간 출력