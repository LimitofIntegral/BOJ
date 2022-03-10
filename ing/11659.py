import sys
input = sys.stdin.readline
print = sys.stdout.write

a, b = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(b):
    i, j = map(int, input().split())
    print(str(sum(arr[i - 1:j])) + "\n")


# pypy3 시간초과 ㅠㅠ