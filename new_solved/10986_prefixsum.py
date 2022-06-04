import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr_ = [0] * m

total, num = 0, 0
for i in range(n):
    total += arr[i]
    result = total % m

    if result == 0:
        num += 1
    
    arr_[result] += 1


for i in range(m):
    if arr_[i]:
        num += arr_[i] * (arr_[i] - 1) // 2

print(num)