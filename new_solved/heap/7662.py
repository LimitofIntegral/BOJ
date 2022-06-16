import heapq as h

def sync():
    while t_M:
        if q_M[0] != t_M[0]:
            break
        h.heappop(q_M)
        h.heappop(t_M)
    while t_m:
        if q_m[0] != t_m[0]:
            break
        h.heappop(q_m)
        h.heappop(t_m)


for _ in range(int(input())):
    q_M, q_m = [], []
    t_M, t_m = [], []
    for _ in range(int(input())):
        c, i = input().split()

        if c == "I":
            h.heappush(q_m, int(i))
            h.heappush(q_M, -int(i))
        else:
            sync()
            if q_M and q_m:
                if i == "1":
                    h.heappush(t_m, -h.heappop(q_M))
                else:
                    h.heappush(t_M, -h.heappop(q_m))
    sync()
    if q_m and q_M:
        print(-q_M[0], q_m[0])
    else:
        print("EMPTY")
    