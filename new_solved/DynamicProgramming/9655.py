n = int(input())

arr = [0] * 1001

for i in range(4, n + 1):
    if not arr[i - 3] and not arr[i - 1]:
        arr[i] = 1

# 꼼수 ㅋㅋ
arr[2] = 1

print("CY" if arr[n] else "SK")