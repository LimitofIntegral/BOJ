import sys
input = sys.stdin.readline

stack = []
n, k = map(int, input().split())

temp = list(input().strip())

for i in temp:
    if stack:
        while stack and k and i > stack[-1]:
            k -= 1
            stack.pop()
        stack.append(i)
    else:
        stack.append(i)

while k:
    stack.pop()
    k -= 1

for i in stack:
    print(i, end="")