from collections import deque

for i in range(int(input())):
    print(f"Case #{i + 1}: ", end="")
    n = int(input())
    task = deque([])
    a = deque(list(map(int, input().split())))

    while a:
        if task:
            if task[0] == a[0] // 4 * 3:
                print(task.popleft(), end = " ")
                a.popleft()
            else:
                task.append(a.popleft())
        else:
            task.append(a.popleft())
