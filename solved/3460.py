T = int(input())

for _ in range(T):
    arr = list(bin(int(input())))[2:]
    for i in range(len(arr)):
        if arr[len(arr) - 1 - i] == "1":
            print(i, end = " ")