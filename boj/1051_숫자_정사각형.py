n,m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, list(input()))))
s = 1
for k in range(1, min(n,m)):
    for i in range(n-k):
        for j in range(m-k):
            if arr[i][j] == arr[i][j+k] == arr[i+k][j] == arr[i+k][j+k]:
                s = max(s, (k+1)**2)
print(s)