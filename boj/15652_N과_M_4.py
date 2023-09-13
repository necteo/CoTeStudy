n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
tmp = []
ans = []

def subSet(idx, N, R):
    if len(tmp) == R:
        ans.append(tmp[:])
        return
    if idx == N:
        return
    tmp.append(arr[idx])
    subSet(idx, N, R)
    tmp.pop()
    subSet(idx+1, N, R)

subSet(0, n, m)
for i in ans:
    print(*i)