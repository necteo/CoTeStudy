import heapq
import sys

N = int(input())
M = int(input())
g = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    g[u].append([v, w])
D = [sys.maxsize]*(N+1)
start, end = map(int, input().split())


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    D[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if D[now] < dist:
            continue
        for v, w in g[now]:
            cost = D[now] + w
            if cost < D[v]:
                D[v] = cost
                heapq.heappush(q, (cost, v))


dijkstra(start)
if D[end] != sys.maxsize:
    print(D[end])
