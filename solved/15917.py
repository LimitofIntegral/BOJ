import sys
input = sys.stdin.readline

for _ in range(int(input())):
    q = input()
    if q == "1":
        print(1)
    else:
        q = int(q)
        print(1 if "1" not in str(bin(q))[3:] else 0)