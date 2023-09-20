from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, list(input().rstrip()))))


def bfs(a,b):
    visit = [[0 for _ in range(m)] for _ in range(n)]
    queue = deque()
    queue.append([a,b])
    cnt = 1
    while queue:
        for _ in range(len(queue)):
            y,x = queue.popleft()
            if visit[y][x] == 0:
                visit[y][x] = 1
                if y == n-1 and x == m-1:
                    return cnt
                if y > 0:
                    if visit[y-1][x] == 0 and arr[y-1][x] == 1:
                        queue.append([y-1,x])
                if x > 0:
                    if visit[y][x-1] == 0 and arr[y][x-1] == 1:
                        queue.append([y,x-1])
                if y < n-1:
                    if visit[y+1][x] == 0 and arr[y+1][x] == 1:
                        queue.append([y+1,x])
                if x < m-1:
                    if visit[y][x+1] == 0 and arr[y][x+1] == 1:
                        queue.append([y,x+1])
        cnt += 1


print(bfs(0,0))