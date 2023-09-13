import sys
input = sys.stdin.readline
N, M = map(int, input().split())
idx = 1
while idx < N:
    idx *= 2
arr = [0 for _ in range(idx*2)]

for i in range(N):
    v = int(input())
    pos = idx+i
    arr[pos] = v
    pos //= 2
    while pos != 0:
        arr[pos] = min(arr[pos * 2], arr[pos * 2 + 1])
        pos //= 2

def solve(pos, cl, cr, left, right):
    if left <= cl and cr <= right:
        return arr[pos]
    if cr < left:
        return sys.maxsize
    if cl > right:
        return sys.maxsize
    v1 = solve(pos*2, cl, (cl+cr)//2, left, right)
    v2 = solve(pos*2+1, (cl+cr)//2+1, cr, left, right)
    return min(v1, v2)

for _ in range(M):
    a, b = map(int, input().split())
    left = a
    right = b
    print(solve(1, 1, idx, left, right))