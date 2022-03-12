n = int(input())

A, B = [], []
cnt = 0

for _ in range(n):
    A.append(list(map(int, input().split())))
for _ in range(n):
    B.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        for k in range(n):
            if A[i][k] and B[k][j]:
                cnt += 1
                break

print(cnt)