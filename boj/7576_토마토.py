from collections import deque
import sys
input = sys.stdin.readline
M, N = map(int, input().split())
dy, dx = [0, 0, -1, 1], [-1, 1, 0, 0]
tomato = []
for _ in range(N):
    tomato.append(list(map(int, input().split())))

def bfs():
    day = -1
    queue = deque()
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 1:
                queue.append([i, j])
    while queue:
        for _ in range(len(queue)):
            y, x = queue.popleft()
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if 0 <= ny < N and 0 <= nx < M:
                    if tomato[ny][nx] == 0:
                        tomato[ny][nx] = 1
                        queue.append([ny, nx])
        day += 1
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 0:
                day = -1
                break
    return day

print(bfs())