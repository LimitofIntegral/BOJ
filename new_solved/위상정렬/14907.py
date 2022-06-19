from collections import deque, defaultdict

gin = defaultdict(list)
gout = defaultdict(list)
ind = {}
time = {}

while True:
    try:
        cmd = input().split()
        task = cmd[0]
        ind[task] = 0
        if len(cmd) == 2:
            time[task] = int(cmd[1])
        else:
            time[task] = int(cmd[1])
            for i in cmd[2]:
                gin[task].append(i)
                gout[i].append(task)
                ind[task] += 1

    except EOFError:
        break

q = deque([i for i in ind if not ind[i]])

s = []
while q:
    to = q.popleft()
    s.append(to)
    for i in gout[to]:
        ind[i] -= 1
        if not ind[i]:
            q.append(i)

result =  0

for i in s:
    if gin[i]:
        w = 0
        for j in gin[i]:
            w = max(w, time[j])
        time[i] += w
    result = max(result, time[i])

print(result)
        