from collections import deque
import re

for _ in range(int(input())):
    c = list(input())
    n = int(input())
    d = deque(re.findall("\d+", input()))
    t = True #뒤집지 않음.
    try:
        for i in c:
            if i == "R":
                if t:
                    t = False
                else:
                    t = True
            else:
                if t:
                    d.popleft()
                else:
                    d.pop()

        if d:
            if t:
                for i in range(len(d)):
                    if i == 0:
                        print("[" + str(d[0]), end = ",")
                    elif i == len(d) - 1:
                        print(str(d[-1]) + "]")
                    else:
                        print(d[i], end = ",")
            else:
                for i in range(len(d)):
                    if i == 0:
                        print("[" + str(d[-1]), end = ",")
                    elif i == len(d) - 1:
                        print(str(d[0]) + "]")
                    else:
                        print(d[len(d) - 1 - i], end = ",")
        else:
            print("[]")
    except:
        print("error")

# 뭐가 반례일까 궁금하네