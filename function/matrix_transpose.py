"""

    n열 m행 행렬 arr(2차원 list)에 대하여,
    n이 더 클 경우, 즉 세로로 길쭉할 때 전치를 수행하는 알고리즘
    결과값으로 가로로 길쭉한 행렬을 반환함
    
"""

def transpose(arr, n, m):
    if n > m:
        temp = []
        for i in range(m):
            line = []
            for j in range(n):
                line.append(arr[j][i])
            temp.append(line)
        return temp
    else:
        return arr