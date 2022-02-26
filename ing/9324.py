import sys
input = sys.stdin.readline

for _ in range(int(input())):
    d = {}
    check = None
    arr = list(input())
    for i in arr:
        if check:
            if i == check:
                d[i] = 1
                check = None
            else:
                print("FAKE")
                break
        else:
            try: 
                if d[i] == 3:
                    check = i
                else:
                    d[i] += 1
            except: 
                d[i] = 1
    if not check:
        print("OK")