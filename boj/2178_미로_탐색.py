import sys
input = sys.stdin.readline
n,m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, list(input().rstrip()))))
visit= [[0 for _ in range(m)] for _ in range(n)]
ans = [10000]
def dfs(a,b,dep):
    visit[a][b] = 1
    if min(ans) < dep:
        return
    if a == n-1 and b == m-1:
        if dep not in ans:
            ans.append(dep)
        return
    if a > 0:
        if visit[a-1][b] == 0 and arr[a-1][b] == 1:
            dfs(a-1,b,dep+1)
            visit[a-1][b] = 0
    if b > 0:
        if visit[a][b-1] == 0 and arr[a][b-1] == 1:
            dfs(a,b-1,dep+1)
            visit[a][b-1] = 0
    if a < n-1:
        if visit[a+1][b] == 0 and arr[a+1][b] == 1:
            dfs(a+1,b,dep+1)
            visit[a+1][b] = 0
    if b < m-1:
        if visit[a][b+1] == 0 and arr[a][b+1] == 1:
            dfs(a,b+1,dep+1)
            visit[a][b+1] = 0
    dep -= 1

dfs(0,0,1)
print(min(ans))