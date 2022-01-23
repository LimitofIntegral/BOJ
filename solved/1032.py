n = int(input())

r = list(input())
l = len(r)

for i in range(n - 1):
    t = list(input())
    for j in range(l):
        if r[j] == "?":
            pass
        else:
            if r[j] != t[j]:
                r[j] = "?"

print("".join(r))