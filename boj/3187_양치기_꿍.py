from collections import deque
r, c = map(int, input().split())
arr = []
for _ in range(r):
    arr.append(list(input()))
visited = [[0 for _ in range(c)] for _ in range(r)]
ans = [0,0]

def bfs(sy, sx):
    queue = deque()
    queue.append([sy,sx])
    k,v = 0,0
    while queue:
        y,x = queue.popleft()
        if visited[y][x] == 0:
            visited[y][x] = 1
            if arr[y][x] == '#':
                continue
            if arr[y][x] == 'k':
                k += 1
            if arr[y][x] == 'v':
                v += 1
            if x > 0:
                queue.append([y,x-1])
            if x < c-1:
                queue.append([y,x+1])
            if y > 0:
                queue.append([y-1,x])
            if y < r-1:
                queue.append([y+1,x])
    if k > v:
        ans[0] += k
    else:
        ans[1] += v

for i in range(r):
    for j in range(c):
        if arr[i][j] == 'v' or arr[i][j] == 'k':
            bfs(i,j)
print(*ans)