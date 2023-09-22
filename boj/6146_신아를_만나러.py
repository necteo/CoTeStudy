from collections import deque
import sys
input = sys.stdin.readline
x,y,n = map(int, input().split())
arr = [[0 for _ in range(1001)] for _ in range(1001)]
for _ in range(n):
    a,b = map(int, input().split())
    arr[500-b][a+500] = 1


def bfs(sx,sy):
    visit = [[0 for _ in range(1001)] for _ in range(1001)]
    queue = deque()
    queue.append([sx+500,500-sy])
    cnt = 0
    while queue:
        for _ in range(len(queue)):
            u,v = queue.popleft()
            if visit[v][u] == 0:
                visit[v][u] = 1
                if v == 500-y and u == x+500:
                    return cnt
                if v > 0:
                    if visit[v-1][u] == 0 and arr[v-1][u] == 0:
                        queue.append([u,v-1])
                if u > 0:
                    if visit[v][u-1] == 0 and arr[v][u-1] == 0:
                        queue.append([u-1,v])
                if v < 1000:
                    if visit[v+1][u] == 0 and arr[v+1][u] == 0:
                        queue.append([u,v+1])
                if u < 1000:
                    if visit[v][u+1] == 0 and arr[v][u+1] == 0:
                        queue.append([u+1,v])
        cnt += 1


print(bfs(0,0))