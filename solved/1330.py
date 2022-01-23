arr = list(map(int, input().split()))
a, b = arr[0], arr[1]


if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")