import re

for _ in range(int(input())):
    cmd = list(input())
    start, end = 0, int(input())
    arr = re.findall("\d+", input())
    t = True # 뒤집지 않은 상태
    for i in cmd:
        if i == "R":
            if t:
                t = False
            else:
                t = True
        else:
            if t:
                start += 1
            else:
                end -= 1

    if start > end:
        print("error")
        continue

    if start == end:
        print("[]")
    elif start + 1 == end:
        print("[" + str(arr[0]) + "]")
    else:
        if t:
            pass