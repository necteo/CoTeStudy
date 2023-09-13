n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)]
tmp = []
ans = []


def perm(idx, N, R):
    if idx == R:
        ans.append(tmp[:])
        return
    for i in range(N):
        tmp.append(arr[i])
        perm(idx + 1, N, R)
        tmp.pop()


perm(0, n, m)
for i in ans:
    print(*i)
