from collections import deque
n, m, v = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
for i in range(n+1):
    arr[i].sort()
visited = [0 for _ in range(n+1)]


def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for i in arr[v]:
        if visited[i] == 0:
            dfs(i)


def bfs(v):
    visited = [0 for _ in range(n+1)]
    visited[v] = 1
    queue = deque()
    queue.append(v)
    while len(queue) != 0:
        w = queue.popleft()
        print(w, end=' ')
        for i in arr[w]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)


dfs(v)
print()
bfs(v)
