import sys
import heapq

N, M, K, X = map(int, input().split())
g = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    g[A].append(B)
D = [sys.maxsize]*(N+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    D[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if D[now] < dist:
            continue
        for v in g[now]:
            cost = D[now] + 1
            if cost < D[v]:
                D[v] = cost
                heapq.heappush(q, (cost, v))

dijkstra(X)
chk = 0
for i in range(1, N+1):
    if D[i] == K:
        print(i)
        chk = 1
if chk == 0:
    print(-1)
