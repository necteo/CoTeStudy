from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
arr = [[] for i in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
p = [i for i in range(n+1)]

def bfs(start):
    visit = [0 for _ in range(n + 1)]
    visit[start] = 1
    queue = deque()
    queue.append(start)
    while queue:
        v = queue.popleft()
        for u in arr[v]:
            if visit[u] == 0:
                visit[u] = 1
                p[u] = v
                queue.append(u)

bfs(1)
for i in range(2, n+1):
    print(p[i])