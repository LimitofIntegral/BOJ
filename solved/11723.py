import sys
input = sys.stdin.readline

S = [0] * 21

for _ in range(int(input())):
    c = input().split()
    if len(c) == 2:
        c, i = c[0], int(c[1])

    if c == "add":
        S[i] = 1
    elif c == "remove":
        S[i] = 0
    elif c == "toggle":
        S[i] ^= 1
    elif c[0] == "all":
        S = [1] * 21
    elif c[0] == "empty":
        S = [0] * 21
    else:
        print(S[i])
