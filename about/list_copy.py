"""

    파이썬에서 list를 복사하는 방법 4가지

    list를 복사할 때 단순히 arr1 = arr2 라고 선언하게 되면 복사가 아닌 참조가 된다.

    이 경우 한 쪽에서 원소를 수정하면 다른쪽도 수정이 되기 때문에

    이렇게 하면 안된다.



    참조 : https://www.afternerd.com/blog/python-copy-list/

"""



# 슬라이싱
arr1 = [1, 2, 3, 4, 5]
arr2 = arr1[:]

# list() 적용
arr2 = list(arr1)

# copy() 적용
# python3 에서 추가됨
arr2 = arr1.copy()

# 연산자 사용
arr2 = [] + arr1