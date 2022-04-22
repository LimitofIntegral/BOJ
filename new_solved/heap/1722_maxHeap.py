import sys
import heapq as h
input = sys.stdin.readline

heap = []

for _ in range(int(input())):
    x = int(input())

    if x:
        h.heappush(heap, -x)
    else:
        if heap:
            print(-h.heappop(heap))
        else:
            print(0)