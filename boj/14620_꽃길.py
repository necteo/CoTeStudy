n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
selected = [[0 for _ in range(n)] for _ in range(n)]
cost = 0
min_cost = 10000

def sel(cnt):
    global cost
    if cnt == 3:
        global min_cost
        min_cost = min(min_cost, cost)
    else:
        for i in range(1, n-1):
            for j in range(1, n-1):
                if selected[i][j] == 0 and selected[i][j-1] == 0 and selected[i][j+1] == 0 and selected[i-1][j] == 0 and selected[i+1][j] == 0:
                    selected[i][j] = 1
                    selected[i][j-1] = 1
                    selected[i][j+1] = 1
                    selected[i-1][j] = 1
                    selected[i+1][j] = 1
                    cost += arr[i][j]+arr[i][j-1]+arr[i][j+1]+arr[i-1][j]+arr[i+1][j]
                    sel(cnt+1)
                    cost -= arr[i][j]+arr[i][j-1]+arr[i][j+1]+arr[i-1][j]+arr[i+1][j]
                    selected[i][j] = 0
                    selected[i][j-1] = 0
                    selected[i][j+1] = 0
                    selected[i-1][j] = 0
                    selected[i+1][j] = 0

sel(0)
print(min_cost)