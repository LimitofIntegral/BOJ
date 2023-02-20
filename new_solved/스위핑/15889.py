import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
d = list(map(int, input().split()))

end = 0
check = True

for i in range(n - 1):
    if x[i] <= end:
        end = max(end, x[i] + d[i])
    else:
        check = False
        break

if x[-1] > end:
    check = False

print("권병장님, 중대장님이 찾으십니다" if check else "엄마 나 전역 늦어질 것 같아")