"""
    재귀로 짜면 뻗음 ㅇㅇ
    재귀로 돌리면 일단 n = 40만 가도 버벅일 것
"""

n = int(input())

a, b = 1, 1

if n == 0:
    print(a)
elif n == 1:
    print(b)
else:
    for _ in range(n - 2):
        a, b = b, a + b
    print(b)