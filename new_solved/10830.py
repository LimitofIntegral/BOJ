def mul(arr1, arr2, n):
    temp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            t = 0
            for k in range(n):
                t += arr1[i][k] * arr2[k][j]
            temp[i][j] = t % 1000
    
    return temp


def power(a, b):
    if b == 1:
        for i in range(n):
            for j in range(n):
                a[i][j] %= 1000
        return a
    
    x = power(a, b // 2)

    if b % 2 == 0:
        return mul(x, x, n)
    
    else:
        return mul(mul(x, x, n), a, n)


n, b = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

for i in power(mat, b):
    print(*i)