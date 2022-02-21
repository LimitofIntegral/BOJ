arr = []
while True:
    n = int(input())
    if n != -1:
        arr += [n]
    else:
        break

print(sum(arr))