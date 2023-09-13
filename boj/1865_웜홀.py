import sys

for _ in range(int(input())):
    n, m, w = map(int, input().split())
    g = [[] for _ in range(n+1)]
    for i in range(m):
        s, e, t = map(int, input().split())
        g[s].append([e, t])
        g[e].append([s, t])
    for i in range(w):
        s, e, t = map(int, input().split())
        g[s].append([e, -t])
    ans = [sys.maxsize] * (n+1)
    ans[1] = 0
    for _ in range(n+1):
        for u in range(1, n+1):
            if ans[u] == sys.maxsize:
                continue
            for v, w in g[u]:
                if ans[v] > ans[u] + w:
                    ans[v] = ans[u] + w
    if ans[1] < 0:
        print("YES")
    else:
        print("NO")