n = int(input())
arr = list(map(int, input().split()))
result = [arr[0]]

for i in range(1, n):
    if arr[i] > result[-1]:
        result.append(arr[i])
    else:
        lb = 0
        while arr[i] > result[lb]:
            lb += 1
        result[lb] = arr[i]

print(len(result))