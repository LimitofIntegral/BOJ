t = list(input())
l = len(t)

r = list(input())
m = len(r) - 1

result = 0

for i in r:
    result += t.index(i) + l ** m
    m -= 1

print(result % 900528)

# 어디가 틀렸을까
