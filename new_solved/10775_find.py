import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def find(n):
    if gate[n] == n:
        return n
    
    gate[n] = find(gate[n])
    return gate[n]


g = int(input())
gate = {i : i for i in range(g + 1)}

p = [int(input()) for _ in range(int(input()))]

result = 0

for i in p:
    t = find(i)
    if not t:
        break

    gate[t] = t - 1
    result += 1

print(result)
