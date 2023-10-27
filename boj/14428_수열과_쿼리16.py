import sys
input = sys.stdin.readline
N = int(input())
idx = 1
while idx < N:
    idx *= 2
arr = [0 for _ in range(idx*2)]
data = list(map(int, input().split()))
for i in range(N):
    pos = idx+i
    arr[pos] = data[i]
    while pos != 1:
        pos //= 2
        if arr[pos*2] <= arr[pos*2+1]:
            arr[pos] = pos*2
        else:
            arr[pos] = pos*2+1

def solve(pos, cl, cr, left, right):
    if left <= cl and cr <= right:
        return arr[pos]
    if cl > right:
        return sys.maxsize
    if cr < left:
        return sys.maxsize
    v1 = solve(pos*2, cl, (cl+cr)//2, left, right)
    v2 = solve(pos*2+1, (cl+cr)//2+1, cr, left, right)
    return