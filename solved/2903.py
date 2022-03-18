n = int(input())
p = 2

while n:
    p *= 2
    p -= 1
    n -= 1

print(p ** 2)