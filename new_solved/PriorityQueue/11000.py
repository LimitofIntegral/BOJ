import heapq as h
import sys
input = sys.stdin.readline

heap, job = [], []

for _ in range(int(input())):
    a, b = map(int, input().split())
    job.append((a, b))

job.sort()

h.heapify(heap)

for i in job:
    if heap:
        if heap[0] <= i[0]:
            h.heapreplace(heap, i[1])
        else:
            h.heappush(heap, i[1])
    else:
        h.heappush(heap, i[1])

print(len(heap))