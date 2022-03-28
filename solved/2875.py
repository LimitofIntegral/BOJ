n, m, k = map(int, input().split())

# 팀 초기화
t = 0

# 여 2이상, 남 1이상일 때 팀 하나씩 추가
while n > 1 and m > 0:
    t += 1
    n -= 2
    m -= 1

# 인턴 보낼 인원에서 잔여인원 미리 뺌
k -= n + m

# 이 때 k가 0이하면 t 그대로 출력
# k가 1이상이면 k를 3으로 나눈 나머지에 따라
# k를 3으로 나눈 몫만큼 뺄지, 몫 + 1만큼 뺄지 판단
if k <= 0:
    print(t)
else:
    if k % 3:
        print(t - (k // 3 + 1))
    else:
        print(t - k // 3)