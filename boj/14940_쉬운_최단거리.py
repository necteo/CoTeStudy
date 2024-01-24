import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
ans = [[-1 for _ in range(m)] for _ in range(n)]
dy, dx = [0, 0, -1, 1], [-1, 1, 0, 0]

queue = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            queue.append([i, j])
            ans[i][j] = 0
        elif arr[i][j] == 0:
            ans[i][j] = 0
while queue:
    y, x = queue.popleft()
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if arr[ny][nx] == 1:
                if ans[ny][nx] == -1:
                    ans[ny][nx] = ans[y][x]+1
                    queue.append([ny, nx])
                elif ans[y][x]+1 < ans[ny][nx]:
                    ans[ny][nx] += 1
                    queue.append([ny, nx])
for i in ans:
    print(*i)