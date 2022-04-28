N, m, M, T, R = map(int, input().split())

t = 0
n = 0
end = False
m_ = m

# R은 1보다 크다. 즉 충분히 긴 시간동안 휴식하면 무조건 m이 된다.
# 따라서 맥박 증가량이 맥박 범위보다 넓으면 불가능함을 떠올릴 수 있다.

if M - m < T:
    print(-1)
else:
    while True:
        t += 1
        if m + T <= M:
            m += T
            n += 1
        else:
            m = max(m_, m - R)

        if n == N:
            end = True
            break
    print(t)