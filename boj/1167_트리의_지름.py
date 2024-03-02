import sys
input = sys.stdin.readline
V = int(input())
arr = [[] for _ in range(V+1)]
for _ in range(V):
    info = list(map(int, map(int, input().split())))
    for i in range(1, len(info)-1, 2):
        arr[info[0]].append([info[i], info[i+1]])

def dfs(v, d):
    global ans
    visited[v] = 1
    ans = max(ans, d)
    for u, w in arr[v]:
        if visited[u] == 0:
            visited[u] = 1
            dfs(u, d+w)
            if w > d:
                d = w

ans = 0
visited = [0 for _ in range(V+1)]
dfs(1, 0)
print(ans)