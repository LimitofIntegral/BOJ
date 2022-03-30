n = int(input())

now = int(input())
result = now
chk = False

for _ in range(n):
    a, b = map(int, input().split())
    now += (a - b)
    result = max(result, now)
    if now < 0:
        chk = True

print(0 if chk else result)