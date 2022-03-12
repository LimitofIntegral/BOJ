"""

    두 행렬의 부울곱을 할거임
    들어오는 두 행렬 A와 B는 모두 n * n차 행렬이라고 가정함

    정사각행렬이 아닐 경우 j나 k를 조정해볼것
    temp.append값 수정하면 단순 행렬곱도 가능할 듯

"""

def product(A, B, n):   # A행렬, B행렬, n차
    C = []
    for i in range(n):
        temp = []
        for j in range(n):
            check = True
            for k in range(n):
                if A[i][k] and B[k][j]:
                    temp.append(1)
                    check = False
                    break
            if check:
                temp.append(0)
        C.append(temp)
    
    return C
