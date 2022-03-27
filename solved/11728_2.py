"""

    굳이 배열에 넣고 정렬할 필요는 없지않을까?
    어차피 입력이 정렬되어 들어오니 비교해서 하나씩 출력해보자...
    시간차이가 얼마나 날지

    결론 - 단순히 두배열 합쳐서 sort : 1832ms
          아래 코드처럼 무지성 반복출력 : 2404ms


"""

n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

i, j = 0, 0

while True:
    if i == n:
        while j < m:
            print(b[j], end = " ")
            j += 1
        break
    elif j == m:
        while i < n:
            print(a[i], end = " ")
            i += 1
        break
    else:
        if a[i] >= b[j]:
            print(b[j], end = " ")
            j += 1
        else:
            print(a[i], end = " ")
            i += 1
    
    if i == n and j == m:
        break
    