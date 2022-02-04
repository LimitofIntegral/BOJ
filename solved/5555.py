f = input()
c = 0

for _ in range(int(input())):
    t = input()
    t *= 2
    if f in t:
        c += 1

print(c)