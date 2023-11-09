import sys
input = sys.stdin.readline
for _ in range(int(input())):
    N, M = map(int, input().split())
    idx = 1
    while idx < N+M:
        idx *= 2
    arr = [0 for _ in range(idx*2)]
    loc = [0] + [N-i for i in range(N)]

    def update(pos):
        while pos != 1:
            pos //= 2
            arr[pos] = arr[pos*2] + arr[pos*2+1]

    def solve(pos, cl, cr, left, right):
        if left <= cl and cr <= right:
            return arr[pos]
        if cl > right:
            return 0
        if cr < left:
            return 0
        v1 = solve(pos*2, cl, (cl+cr)//2, left, right)
        v2 = solve(pos*2+1, (cl+cr)//2+1, cr, left, right)
        return v1 + v2

    for i in range(N):
        pos = idx+i
        arr[pos] = 1
        update(pos)
    selects = list(map(int, input().split()))
    ans = []
    for i in selects:
        ans.append(solve(1, 1, idx, loc[i]+1, N))
        pos = idx+loc[i]-1
        arr[pos] = 0
        update(pos)
        N += 1
        loc[i] = N
        pos = idx+loc[i]-1
        arr[pos] = 1
        update(pos)
    print(*ans)