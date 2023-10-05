n = int(input())
tp = [[0,0]]
for _ in range(n):
    t,p = map(int, input().split())
    tp.append([t,p])
arr = [0 for _ in range(n+1)]
for i in range(1, n+1):
    if i+tp[i][0]-1 <= n:
        arr[i+tp[i][0]-1] = max(arr[i-1]+tp[i][1], arr[i+tp[i][0]-1])
    arr[i] = max(arr[i-1], arr[i])
print(max(arr))