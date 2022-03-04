"""
    dis 모듈 - 파이썬 바이트 코드 역 어셈블러

    주어진 함수 
    myfunc(alist):
        return len(alist)
    에 대하여

    dis.dis(myfunc)를 사용해 역 어셈블리를 보일 수 있다.    

    https://docs.python.org/ko/3.8/library/dis.html
"""

import dis

def myfunc(alist):
    return len(alist)

dis.dis(myfunc)

"""
     15           0 LOAD_GLOBAL              0 (len)
                  2 LOAD_FAST                0 (alist)
                  4 CALL_FUNCTION            1
                  6 RETURN_VALUE
"""