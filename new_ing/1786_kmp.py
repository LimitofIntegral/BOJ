import sys
input = sys.stdin.readline

idx = []

t = input().replace('\n', '')
p = input().replace('\n', '')

lt = len(t)
lp = len(p)

k = [0] * len(p)

j = 0
for i in range(1, lp):
    while j > 0 and p[i] != p[j]:
        j = k[j - 1]
    if p[i] == p[j]:
        j += 1
        k[i] = j
  
j = 0
for i in range(lt):
    while j > 0 and t[i] != p[j]:
        j = k[j - 1]
    if t[i] == p[j]:
        if j == lp - 1:
            idx.append(i - lp + 2)
            j = k[j]
        else:
            j += 1

print(len(idx))
for i in idx:
    print(i, end = " ")