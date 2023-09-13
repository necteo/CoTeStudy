def find(x, y):
    if visited[y][x] == 0:
        visited[y][x] = 1
        if arr[y][x] == 0:
            return 0
        if x < m-1 and arr[y][x+1] == 1:
            find(x+1, y)
        if x > 0 and arr[y][x-1] == 1:
            find(x-1, y)
        if y < n-1 and arr[y+1][x] == 1:
            find(x, y+1)
        if y > 0 and arr[y-1][x] == 1:
            find(x, y-1)
        return 1
    return 0


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            cnt += find(j, i)
    print(cnt)
