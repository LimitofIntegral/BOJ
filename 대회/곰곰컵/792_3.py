n = int(input())
s = input()
C = 0

for i in s:
    if i == "C":
        C += 1

X = n - C

if C:
    if X:
        if C % (X + 1):
            print(C // (X + 1) + 1)
        else:
            print(C // (X + 1))
    else:
        print(C)
else:
    print(0)