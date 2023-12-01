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
    ans = [100000000]*(N+1)
    ans[1] = 0
    loop = False
    for k in range(N):
        for u in range(1, N+1):
            for v, w in g[u]:
                if ans[v] > ans[u] + w:
                    ans[v] = ans[u] + w
                    if k == N-1:
                        loop = True
    if loop:
        print("YES")
    else:
        print("NO")