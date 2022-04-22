arr = [0] * 1500001
arr[1] = 1

for i in range(2, 1500001):
    arr[i] = (arr[i - 1] + arr[i - 2]) % 1000000

n = int(input())

if n <= 1500000:
    print(arr[n])
else:
    print(arr[n % 1500000])

a, b = 0, 1
n = int(input())
n %= 1500000

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    for _ in range(n - 1):
        a, b = b, (a + b) % 1000000
    print(b)