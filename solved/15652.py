from itertools import product
import re
import sys
N, M = map(int, input().split())

arr = [i for i in range(1, N + 1)]

for i in product(arr, repeat = M):
    check = False
    for j in range(M):
        if j == 0:
            pass
        else:
            if i[j - 1] > i[j]:
                check = True
                break
    
    if check:
        pass
    else:
        for j in i:
            print(j, end = " ")
        print()