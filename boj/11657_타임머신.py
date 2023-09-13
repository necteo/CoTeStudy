import sys

n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append([b, c])
ans = [sys.maxsize] * (n+1)
ans[1] = 0
for _ in range(n-1):
    for u in range(1, n+1):
        if ans[u] == sys.maxsize:
            continue
        for v, w in g[u]:
            if ans[v] > ans[u] + w:
                ans[v] = ans[u] + w
flg = 0
for u in range(1, n+1):
    if ans[u] == sys.maxsize:
        continue
    for v, w in g[u]:
        if ans[v] > ans[u] + w:
            flg = 1
if flg == 0:
    for u in range(2, n+1):
        if ans[u] == sys.maxsize:
            print(-1)
        else:
            print(ans[u])
else:
    print(-1)