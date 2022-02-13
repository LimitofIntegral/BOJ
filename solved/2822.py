arr = []
result = 0

for i in range(8):
    arr.append((int(input()), i + 1))

arr.sort(reverse=True)
arr = arr[:5]

for i in arr:
    result += i[0]

arr.sort(key=lambda x : x[1])

print(result)

for i in arr:
    print(i[1], end=" ")
