n = int(input())

A, B = [], []
cnt = 0

for _ in range(n):
    A.append(list(map(int, input().split())))
for _ in range(n):
    B.append(list(map(int, input().split())))

for i in A:
    for j in range(n):
        for k in B:
            if i[j] and k[j]:
                cnt += 1
                break

print(cnt)

# 비교문 수정 필요