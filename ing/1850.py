import math

a, b = map(int, input().split())

a = int("1" * a)
b = int("1" * b)

print(math.gcd(a, b))

# 500000000000000000 500000000000000002 케이스에서
# 변환 과정에서 메모리 에러
# 다른 방법은?