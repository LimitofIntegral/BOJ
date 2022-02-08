a = list(map(int, input().split()))
b = list(map(int, input().split()))

sa, sb = 0, 0
at, bt = False, False

for i in range(10):
    if a[i] > b[i]:
        sa += 3
        at, bt = True, False
    elif a[i] < b[i]:
        sb += 3
        at, bt = False, True
    else:
        sa += 1
        sb += 1

print(sa, sb)

if sa > sb:
    print("A")
elif sa < sb:
    print("B")
else:
    if at:
        print("A")
    elif bt:
        print("B")
    else:
        print("D")