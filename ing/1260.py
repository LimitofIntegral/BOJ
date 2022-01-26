from queue import Queue

def BFS(graph, start):
    node = Queue()
    temp = graph[start]
    for i in temp:
        node.put(i)
    visit = [start]

    while node:
        visit.append(node.get())
        temp = graph[visit[-1]]
        for i in temp:
            if i not in visit and i not in node:
                node.put(i)
    
    for i in visit:
        print(i, end = " ")


n, m, s = map(int, input().split())

graph = {}

for i in range(m):
    a, b = map(int, input().split())

    try: 
        graph[a].append(b)
    except:
        graph[a] = [b]
    
    try:
        graph[b].append(a)
    except:
        graph[b] = [a]

for i in graph:
    graph[i].sort()

BFS(graph, s)