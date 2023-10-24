import sys
input = sys.stdin.readline
N, M = map(int, input().split())
idx = 1
while idx < N:
    idx *= 2
# 0은 범위 밖 이라서 solve 에서 maxsize 로 바뀜
arr_min = [0 for _ in range(idx*2)]
arr_max = [0 for _ in range(idx*2)]

for i in range(N):
    v = int(input())
    pos = idx+i
    arr_min[pos] = v
    arr_max[pos] = v
    while pos != 1:
        pos //= 2
        arr_min[pos] = min(arr_min[pos*2], arr_min[pos*2+1])
        arr_max[pos] = max(arr_max[pos*2], arr_max[pos*2+1])

def solve(pos, cl, cr, left, right):
    if left <= cl and cr <= right:
        return arr_min[pos], arr_max[pos]
    if cr < left:
        return sys.maxsize, 0
    if cl > right:
        return sys.maxsize, 0
    vn1, vx1 = solve(pos*2, cl, (cl+cr)//2, left, right)
    vn2, vx2 = solve(pos*2+1, (cl+cr)//2+1, cr, left, right)
    return min(vn1, vn2), max(vx1, vx2)

for _ in range(M):
    a, b = map(int, input().split())
    print(*solve(1, 1, idx, a, b))