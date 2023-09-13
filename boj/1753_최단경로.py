import heapq
import sys

V, E = map(int, input().split())
start = int(input())
g = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    g[u].append([v, w])
D = [sys.maxsize] * (V+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    D[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if D[now] < dist:   # start에서 now까지의 최소비용거리 D[now]가 now의 거리가 작을경우
            continue
        for v, w in g[now]:
            cost = D[now] + w
            if cost < D[v]:
                D[v] = cost
                heapq.heappush(q, (cost, v))
dijkstra(start)
for i in range(1, V+1):
    if D[i] == sys.maxsize:
        print("INF")
    else:
        print(D[i])
