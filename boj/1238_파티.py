from collections import deque
import sys
input = sys.stdin.readline
N, M, X = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])

def bfs(start, end):
    visited = [0 for _ in range(N+1)]
    visited[start] = 1
    queue = deque()
    queue.append(start)
    s = 0
    while queue:
        v = queue.popleft()
        for u, t in arr[v]:
            if visited[u] == 0:
                visited[u] = 1
                s += t
                if u == end:
                    return s
                queue.append(u)

ans = 0
for i in range(1, N+1):
    if i != X:
        total = bfs(i, X)+bfs(X, i)
        print(total)
        ans = max(ans, total)
print(ans)