n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
chk = [0 for _ in range(n)]
tmp = []


def perm(idx, N, R):
    if idx == R:
        for v in tmp:
            print(v, end=" ")
        print()
        return
    s = 0
    for i in range(N):
        if chk[i] == 0 and s != arr[i]:
            chk[i] = 1
            tmp.append(arr[i])
            s = arr[i]
            perm(idx+1, N, R)
            tmp.pop()
            chk[i] = 0


perm(0, n, m)
