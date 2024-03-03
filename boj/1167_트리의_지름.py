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
    s = [0]
    for u, w in arr[v]:
        if visited[u] == 0:
            visited[u] = 1
            s.append(dfs(u, w))
    if len(s) > 1:
        s.sort()
        ans = max(ans, s[-2]+s[-1])
        return d+s[-1]
    ans = max(ans, d+s[-1])
    return d+s[-1]

ans = 0
visited = [0 for _ in range(V+1)]
dfs(1, 0)
print(ans)