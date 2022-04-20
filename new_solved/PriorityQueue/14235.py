import sys
import heapq as h
input = sys.stdin.readline

heap = []

for _ in range(int(input())):
    temp = list(map(int, input().split()))
    if len(temp) == 1:
        if heap:
            print(-h.heappop(heap))
        else:
            print(-1)
    else:
        for i in range(temp[0]):
            h.heappush(heap, -temp[i + 1])
