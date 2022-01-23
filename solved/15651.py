from itertools import product
import re
import sys
N, M = map(int, input().split())

arr = [i for i in range(1, N + 1)]

for i in product(arr, repeat = M):
    temp = str(i)
    temp = re.findall(r'\d', temp)
    for j in temp:
        sys.stdout.write(j + " ")
    sys.stdout.write("\n")