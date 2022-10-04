def check(arr):
    for i in arr:
        for j in i:
            if j != 0:
                return False
    return True


def part(arr, size):
    global step
    m = size // 2

    if m == 1:
        cnt = 0
        for i in range(2):
            for j in range(2):
                if not arr[i][j]:
                    cnt += 1

        if cnt != 3:
            print(-1)
            exit()

        for i in range(2):
            for j in range(2):
                if arr[i][j] == 0:
                    arr[i][j] = step
        step += 1
        return arr
    

    lu = [i[:m] for i in arr[:m]]
    ru = [i[m:] for i in arr[:m]]
    ld = [i[:m] for i in arr[m:]]
    rd = [i[m:] for i in arr[m:]]

    if check(lu):
        lu[-1][-1] = step
    
    if check(ru):
        ru[-1][0] = step
    
    if check(ld):
        ld[0][-1] = step
    
    if check(rd):
        rd[0][0] = step

    step += 1

    lu = part(lu, m)
    ru = part(ru, m)
    ld = part(ld, m)
    rd = part(rd, m)

    result = []

    for i, j in zip(lu, ru):
        result.append(i + j)
    
    for i, j in zip(ld, rd):
        result.append(i + j)
    
    return result
    
step = 1
n = int(input())
arr = [[0] * 2 ** n for _ in range(2 ** n)]
x, y = map(int, input().split())
arr[y - 1][x - 1] = -1

result = part(arr, 2 ** n)
for i in range(1, 2 ** n + 1):
    print(*result[-i])