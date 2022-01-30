n, w, h = map(int, input().split())

s = (w ** 2 + h ** 2) ** 0.5

for _ in range(n):
    if int(input()) > s:
        print("NE")
    else:
        print("DA")