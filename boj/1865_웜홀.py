import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, M, W = map(int, input().split())
    g = [[] for _ in range(N+1)]
    for i in range(M):
        s, e, t = map(int, input().split())
        g[s].append([e, t])
        g[e].append([s, t])
    for i in range(W):
        s, e, t = map(int, input().split())
        g[s].append([e, -t])
    loop = []
    for i in range(1, N+1):
        ans = [sys.maxsize]*(N+1)
        ans[i] = 0
        for k in range(N+1):
            for u in range(1, N+1):
                if ans[u] == sys.maxsize:
                    continue
                for v, w in g[u]:
                    if ans[v] > ans[u] + w:
                        ans[v] = ans[u] + w
            if k == N:
                loop.append(True)
    if True in loop:
        print("YES")
    else:
        print("NO")