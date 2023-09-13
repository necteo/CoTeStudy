arr = []
for _ in range(5):
    arr.append(list(map(int, input().split())))
ans = []

def dfs(num,x,y,dep):
    num.append(arr[y][x])
    if dep == 5:
        if num not in ans:
            ans.append(num.copy())
        num.pop()
        return
    if x < 4:
        dfs(num, x+1, y, dep + 1)
    if x > 0:
        dfs(num, x-1, y, dep + 1)
    if y < 4:
        dfs(num, x, y+1, dep + 1)
    if y > 0:
        dfs(num, x, y-1, dep + 1)
    num.pop()

for i in range(5):
    for j in range(5):
        dfs([], j, i, 0)
print(len(ans))