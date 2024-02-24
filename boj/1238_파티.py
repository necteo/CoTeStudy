import heapq
import sys
input = sys.stdin.readline
N, M, X = map(int, input().split())
g = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    g[a].append([b, c])

def dijkstra(start, end):
    d = [sys.maxsize]*(N+1)
    q = []
    heapq.heappush(q, (0, start))
    d[start] = 0

    while q:
        t, now = heapq.heappop(q)
        if d[now] < t:
            continue
        for v, w in g[now]:
            time = d[now]+w
            if time < d[v]:
                d[v] = time
                heapq.heappush(q, (time, v))
    return d[end]

ans = 0
for i in range(1, N+1):
    if i != X:
        ans = max(ans, dijkstra(i, X)+dijkstra(X, i))
print(ans)