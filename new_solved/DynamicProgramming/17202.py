A = list(map(int, list(input())))
B = list(map(int, list(input())))

result = [0] * 16

for i in range(8):
    result[0 + i * 2] = A[i]
    result[1 + i * 2] = B[i]

for i in range(14):
    temp = []
    for j in range(15 - i):
        temp.append((result[j] + result[j + 1]) % 10)
    result = temp

print(str(result[0]) + str(result[1]))