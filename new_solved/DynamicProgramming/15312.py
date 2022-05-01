a = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
b = [chr(65 + i) for i in range(26)]
d = {b[i] : a[i] for i in range(26)}

A = list(input())
B = list(input())

result = [0] * len(A) * 2

for i in range(len(A)):
    result[0 + 2 * i] = d[A[i]]
    result[1 + 2 * i] = d[B[i]]

p = len(result)

for i in range(p - 2):
    temp = []
    for j in range(p - 1 - i):
        temp.append((result[j] + result[j + 1]) % 10)
    result = temp
    
print(str(result[0]) + str(result[1]))