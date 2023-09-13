n, k = map(int, input().split())
maxv = [[0 for _ in range(k+1)] for _ in range(n+1)]
ans = 0
for i in range(1, n+1):
    w, v = map(int, input().split())
    for j in range(1, k+1):
        if j < w:
            maxv[i][j] = maxv[i-1][j]
            continue
        if maxv[i-1][j-w] + v > maxv[i-1][j]:
            maxv[i][j] = maxv[i-1][j-w] + v
        else:
            maxv[i][j] = maxv[i-1][j]
        ans = maxv[i][j]
    print(maxv[i])
print(ans)