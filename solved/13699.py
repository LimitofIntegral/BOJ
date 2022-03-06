t = [1, 1]

n = int(input())

if n == 0:
    print(1)
elif n == 1:
    print(1)
else:
    for i in range(2, n + 1):
        temp = 0
        for j in range(i // 2):
            temp += 2 * t[j] * t[i - 1 - j]
        if i % 2:
            temp += t[i // 2] ** 2
        t.append(temp)
    print(t[-1])