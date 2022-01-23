arr = list(map(int, input().split()))

k = min(arr) - 1
count = 0

while count < 3:
    count = 0
    k += 1
    for i in arr:
        if k % i == 0:
            count += 1

print(k)