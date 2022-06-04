import sys
sys.setrecursionlimit(10**5)

def post(l, r):
    if l > r:
        return
    m = r + 1
    for i in range(l + 1, r + 1):
        if arr[l] < arr[i]:
            m = i
            break
    
    post(l + 1, m - 1)
    post(m, r)
    print(arr[l])

arr = []

while True:
    try:
        arr.append(int(input()))
    except EOFError:
        break

post(0, len(arr) - 1)
