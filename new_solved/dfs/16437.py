import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start, before = -1):
    result = 0
    stack = graph[start][2]

    if len(stack) == 1 and stack[0] == before:
        if graph[start][0] == 'S':
            return graph[start][1]
        else:
            return 0

    if not graph[start][0]:
        for i in stack:
            result += dfs(i, start)
        return result
    else:
        if graph[start][0] == 'S':
            for i in stack:
                if i != before:
                    result += dfs(i, start)
            return result + graph[start][1]
        else:
            for i in stack:
                if i != before:
                    result += dfs(i, start)
            if result <= graph[start][1]:
                return 0
            else:
                return result - graph[start][1]


n = int(input())
graph = {i + 1 : [None, 0, []] for i in range(n)}

for i in range(2, n + 1):
    temp = list(input().split())
    t, a, p = temp[0], int(temp[1]), int(temp[2])
    graph[i][0], graph[i][1] = t, a
    graph[i][2].append(p)
    graph[p][2].append(i)

print(dfs(1))