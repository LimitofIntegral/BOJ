a, b = map(int, input().split())

while a != 0 and b != 0:
    v1 = a // b
    v2 = a % b
    print(v1, v2, "/", b)
    a, b = map(int, input().split())