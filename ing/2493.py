import sys
input = sys.stdin.readline

stack = []

n = int(input())
tower = list(map(int, input().split()))

for i in range(n):
    if not i:
        stack.append(i)
        print(0, end = " ")
    else:
        pass