N = int(input())

arr = list(map(int, input().split()))

count = {}
for i in arr:
    try: count[i] += 1
    except: count[i] = 1

M = int(input())

arr = list(map(int, input().split()))

for i in arr:
    print(count[i] if i in count else 0, end = " ")