cnt = [1, 0]

n = int(input())

for _ in range(n):
    a = cnt[0]
    b = cnt[1]
    cnt = [b, a + b]

print(cnt[0], cnt[1])