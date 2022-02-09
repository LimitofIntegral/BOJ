import itertools

arr = [i + 1 for i in range(int(input()))]
P = list(itertools.permutations(arr))

print(P)