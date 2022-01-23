import sys
input = sys.stdin.readline

N = int(input())

arr = [int(input()) for _ in range(N)]
arr.sort()

count = {}
for i in arr:
    try: count[i] += 1
    except: count[i] = 1

key = []
m = 0

for i in count:
    if m == count[i]:
        key.append(i)
    if m < count[i]:
        key = [i]
        m = count[i]

print(round(sum(arr) / N))
print(arr[N // 2])
if len(key) == 1:
    print(key[0])
else:
    print(key[1])
print(arr[-1] - arr[0])
