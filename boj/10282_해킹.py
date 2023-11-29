import heapq
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, d, c = map(int, input().split())
    g = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        g[b].append([a, s])
    D = [sys.maxsize]*(n+1)

    q = []
    heapq.heappush(q, (0, c))
    D[c] = 0

    while q:
        dist, now = heapq.heappop(q)
        if D[now] < dist:
            continue
        for v, t in g[now]:
            cost = D[now] + t
            if cost < D[v]:
                D[v] = cost
                heapq.heappush(q, (cost, v))

    cnt = 0
    m = 0
    for i in D:
        if i < sys.maxsize:
            cnt += 1
            if m < i:
                m = i
    print(cnt, m)