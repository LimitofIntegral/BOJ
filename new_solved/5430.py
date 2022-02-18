from collections import deque
import re

for _ in range(int(input())):
    c = list(input())
    n = int(input())
    d = deque(re.findall("\d+", input())) # 입력 문자열에서 숫자만 골라 받을수 있는 테크닉
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
            if len(d) == 1:
                print("[" + str(d[0]) + "]")
            else:
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

# 뭐가 반례일까 궁금하네 >> ㅋㅋ 개수가 1개일 때를 까먹음