import sys
input = sys.stdin.readline

s = input().strip()
e = input().strip()

ls, le = len(s), len(e)
stack = []

for i in s:
    stack.append(i)
    if i == e[-1]:
        if ''.join(stack[-le:]) == e:
            for _ in range(le):
                stack.pop()

print(''.join(stack) if stack else "FRULA")
