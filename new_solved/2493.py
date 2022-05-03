n = int(input())
tower = list(map(int, input().split()))
result = [0] * n
stack, m = [0], tower[0]

for i in range(1, n):
    p = tower[i]
    if m <= p:
        stack, m = [i], p
    else:
        while tower[stack[-1]] <= p:
            stack.pop()
        result[i] = stack[-1] + 1
        stack.append(i)

print(*result)