import sys
input = sys.stdin.readline

n = int(input())
result = 0
arr = list(map(int, input().split()))
for i in arr:
    for j in arr:
        result += abs(i - j)
print(result)