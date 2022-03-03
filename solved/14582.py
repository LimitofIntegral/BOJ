a = list(map(int, input().split()))
b = list(map(int, input().split()))

sa, sb = 0, 0
chk = False

for i in range(9):
    sa += a[i]
    if sa > sb:
        chk = True
        break
    sb += b[i]

if chk:
    print("Yes")
else:
    print("No")