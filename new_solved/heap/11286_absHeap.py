import sys
import heapq as h
input = sys.stdin.readline

heap = []

for _ in range(int(input())):
    x = int(input())

    if x:
        if x < 0 :
            h.heappush(heap, (-x, 0))
        else:
            h.heappush(heap, (x, 1))
    else:
        if heap:
            t = h.heappop(heap)
            if t[1]:
                print(t[0])
            else:
                print(-t[0])
        else:
            print(0)