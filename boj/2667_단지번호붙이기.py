from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, list(input().rstrip()))))
visit = [[0 for _ in range(n)] for _ in range(n)]
ans = []

def bfs(a,b):
    queue = deque()
    queue.append([a,b])
    num = 0
    while queue:
        y, x = queue.popleft()
        if visit[y][x] == 0:
            visit[y][x] = 1
            if arr[y][x] == 1:
                num += 1
            else:
                return
            if y > 0:
                if arr[y - 1][x] == 1:
                    queue.append([y - 1, x])
            if x > 0:
                if arr[y][x - 1] == 1:
                    queue.append([y, x - 1])
            if y < n - 1:
                if arr[y + 1][x] == 1:
                    queue.append([y + 1, x])
            if x < n - 1:
                if arr[y][x + 1] == 1:
                    queue.append([y, x + 1])
    if num != 0:
        ans.append(num)

for i in range(n):
    for j in range(n):
        bfs(i,j)
ans.sort()
print(len(ans))
for i in ans:
    print(i)