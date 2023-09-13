n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
chk = [0 for _ in range(n)]
tmp = []
ans = []


def perm(idx, N, R):
    if idx == R:
        ans.append(tmp[:])
        return
    for i in range(N):
        if chk[i] == 0:
            chk[i] = 1
            tmp.append(arr[i])
            perm(idx+1, N, R)
            tmp.pop()
            chk[i] = 0


perm(0, n, m)
for i in ans:
    print(*i)