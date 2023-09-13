n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
tmp = []
ans = []


def perm(idx, N, R):
    if len(tmp) == R:
        ans.append(tmp[:])
        return
    if idx == N:
        return
    tmp.append(arr[idx])
    perm(idx+1, N, R)
    tmp.pop()
    perm(idx+1, N, R)


perm(0, n, m)
for i in ans:
    print(*i)