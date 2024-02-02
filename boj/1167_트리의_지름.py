import sys
input = sys.stdin.readline
V = int(input())
arr = [[] for _ in range(V+1)]
for _ in range(V):
    info = list(map(int, map(int, input().split())))
    for i in range(1, len(info)-1, 2):
        arr[info[0]].append([info[i], info[i+1]])

def solve(v):
    global d, ans
    visited[v] = 1
    for u, w in arr[v]:
        if visited[u] == 0:
            visited[u] = 1
            d += w
            solve(u)
            d -= w
    ans = max(d, ans)

ans = 0
for i in range(1, V+1):
    d = 0
    visited = [0 for _ in range(V+1)]
    solve(i)
print(ans)