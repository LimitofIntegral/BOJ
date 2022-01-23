"""
단순히 arr = arr[1:] 로 pop을 구현하자니 오류가 나더라.
deque 사용이 강제된다고 봐야할 듯.
더불어 출력도 그냥 print로는 안됨.
"""
import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

cmd = {"pop" : 0, "size" : 1, "empty" : 2, "front" : 3, "back" : 4}
arr = deque()

N = int(input())

for _ in range(N):
    temp = input()
    
    if "pu" in temp:
        arr.append(temp.split()[1])
    else:
        s = cmd[temp.rstrip()]

        if s == 0:
            if len(arr) != 0:
                print(arr.popleft() + "\n")
            else:
                print("-1\n")
        elif s == 1:
            print(str(len(arr)) + "\n")
        elif s == 2:
            print("0\n" if len(arr) else "1\n")
        elif s == 3:
            print(arr[0] + "\n" if len(arr) else "-1\n")
        elif s == 4:
            print(arr[-1] + "\n" if len(arr) else "-1\n")