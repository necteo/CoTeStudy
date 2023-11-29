import heapq
import sys

for _ in range(int(input())):
    n, d, c = map(int, input().split())
    g = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        g[b].append([a, s])
    D = [sys.maxsize]*(n+1)

    q = []
    heapq.heappush(q, (0, c))

    while q:
        dist, now = heapq.heappop(q)
        if D[now] < dist:
            continue
