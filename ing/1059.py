l = int(input())
arr = list(map(int, input().split()))
n = int(input())

arr.sort()
result = 0

if n in arr:
    print(0)
else:
    for i in range(l):
        a = arr[i]
        b = arr[i + 1]
        if n < a:
            b = a
            a = 0
            break
        if a < n and n < b:
            break
 
    print(a, b)
    
    v1 = n - a - 1
    v2 = b - n
    
    print(v1 * v2 + v2 - 1)

"""

뭐가 틀렸을까?? 구간문제??

"""