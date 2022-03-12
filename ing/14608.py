def calc(c, n): #계수와 차수
    n += 1
    c /= n

    return c, n

print(calc(3, 1))

k = int(input())
c1, c2 = map(int, input().split())
a, b, n = map(int, input().split())

