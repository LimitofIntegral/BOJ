temp = list(input())
result = []
stack = []

for i in temp:
    if i.isalpha():
        result.append(i)
    else:
        if i == '(':
            stack.append(i)
        elif i in ('*', '/'):
            while stack and stack[-1] in ('*', '/'):
                result.append(stack.pop())
            stack.append(i)
        elif i in ('+', '-'):
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.append(i)
        else:
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()

while stack:
    result.append(stack.pop())

for i in result:
    print(i, end = "")