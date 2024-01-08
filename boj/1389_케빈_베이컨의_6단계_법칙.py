import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def bfs(start):
    visit = [0 for _ in range(N+1)]
    visit[start] = 1
    queue = deque()
    queue.append(start)
    bacon = 0
    lvl = 1
    while queue:
        for _ in range(len(queue)):
            v = queue.popleft()
            for w in arr[v]:
                if visit[w] == 0:
                    visit[w] = 1
                    queue.append(w)
                    bacon += lvl
        lvl += 1
    return bacon

ans = 0
m = sys.maxsize
for i in range(1, N+1):
    res = bfs(i)
    if res < m:
        ans = i
        m = res
print(ans)