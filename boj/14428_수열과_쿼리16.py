import sys
input = sys.stdin.readline
N = int(input())
idx = 1
while idx < N:
    idx *= 2
arr = [[0, 0] for _ in range(idx*2)]
data = list(map(int, input().split()))
for i in range(N):
    pos = idx+i
    arr[pos] = [data[i], i+1]
    while pos != 1:
        pos //= 2
        if arr[pos*2][0] <= arr[pos*2+1][0]:
            arr[pos] = arr[pos*2]
        else:
            arr[pos] = arr[pos*2+1]


def solve(pos, cl, cr, left, right):
    if left <= cl and cr <= right:
        return arr[pos]
    if cl > right:
        return [sys.maxsize, 0]
    if cr < left:
        return [sys.maxsize, 0]
    v1 = solve(pos*2, cl, (cl+cr)//2, left, right)
    v2 = solve(pos*2+1, (cl+cr)//2+1, cr, left, right)
    if v1[0] <= v2[0]:
        return v1
    else:
        return v2

M = int(input())
for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 1:
        pos = idx+b-1
        arr[pos] = [c, b]
        while pos != 1:
            pos //= 2
            if arr[pos*2][0] <= arr[pos*2+1][0]:
                arr[pos] = arr[pos*2]
            else:
                arr[pos] = arr[pos*2+1]
    elif a == 2:
        print(solve(1, 1, idx, b, c)[1])
