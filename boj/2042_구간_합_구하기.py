N, M, K = map(int, input().split())
idx = 1
while idx < N:
    idx *= 2
arr = [0 for _ in range(idx*2)]

def update(pos):
    while pos != 0:
        arr[pos] = arr[pos*2] + arr[pos*2+1]
        pos //= 2

for i in range(N):
    v = int(input())
    pos = idx+i
    arr[pos] = v
    pos //= 2
    update(pos)

def solve(pos, cl, cr, left, right):
    if left <= cl and cr <= right:
        return arr[pos]
    if cr < left:
        return 0
    if cl > right:
        return 0
    v1 = solve(pos*2, cl, (cl+cr)//2, left, right)
    v2 = solve(pos*2+1, (cl+cr)//2+1, cr, left, right)
    return v1 + v2

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        pos = idx+b-1
        arr[pos] = c
        pos //= 2
        update(pos)
    elif a == 2:
        left = b
        right = c
        print(solve(1, 1, idx, left, right))



def version1():
    for i in range(N):
        v = int(input())
        pos = idx + i
        while pos != 0:
            arr[pos] += v
            pos //= 2