import sys
input = sys.stdin.readline
N, M, B = map(int, input().split())
arr = []
for _ in range(N):
    arr.extend(list(map(int, input().split())))
arr.sort(reverse=True)
ans = []
for h in range(arr[0], arr[-1]-1, -1):
    tB = B
    t = 0
    for i in range(N*M):
        if arr[i] < h:
            tB -= (h-arr[i])
            t += (h-arr[i])
        elif arr[i] > h:
            tB += (arr[i]-h)
            t += (arr[i]-h)*2
        if tB < 0:
            break
    if tB >= 0:
        ans.append((t, h))
ans.sort(key=lambda x: x[0])
print(*ans[0])