from collections import deque
import sys
input = sys.stdin.readline
M, N = map(int, input().split())
tomato = []
for _ in range(N):
    tomato.append(list(map(int, input().split())))

def bfs():
    visited = [[0 for _ in range(M)] for _ in range(N)]
    day = -1
    queue = deque()
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 1:
                if visited[i][j] == 0:
                    visited[i][j] = 1
                    queue.append([i, j])
    for _ in range(len(queue)):
        while queue:
            y, x = queue.popleft()
            if x > 0 and tomato[y][x-1] == 0:
                queue.append([y, x-1])
            elif x < M-1 and tomato[y][x+1] == 0:
                queue.append([y, x+1])
            elif y > 0 and tomato[y-1][x] == 0:
                queue.append([y-1, x])
            elif y < N-1 and tomato[y+1][x] == 0:
                queue.append([y+1, x])
        day += 1
    return day

print(bfs())