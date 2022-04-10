def check(arr, p):
    for i in arr:
        for j in i:
            if j != p:
                return False, -1
    return True, p

def qt(arr):
    global result

    if len(arr) == 1:
        if arr[0][0] == "1":
            result += "1"
        else:
            result += "0"
    else:
        temp = check(arr, arr[0][0])
        if temp[0]:
            result += str(temp[1])
        else:
            p = len(arr) // 2
            result += "("
            up = arr[:p]
            down = arr[p:]
            lu = [i[:p] for i in up]
            ru = [i[p:] for i in up]
            ld = [i[:p] for i in down]
            rd = [i[p:] for i in down]
            qt(lu)
            qt(ru)
            qt(ld)
            qt(rd)
            result += ")"


result = ""

n = int(input())
arr = [list(input()) for _ in range(n)]

qt(arr)
print(result)