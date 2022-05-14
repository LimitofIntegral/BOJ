import sys
input = sys.stdin.readline
result = 0
for _ in range(int(input())):
    s = input()
    if s == "ENTER":
        d = {}
    else:
        if s in d:
            pass
        else:
            result += 1
            d[s] = None

print(result)