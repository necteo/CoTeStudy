import sys
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    s, e = map(int, input().split())
    arr.append((s, e))
arr.sort()
dp = [arr[0]]
for i in range(1, N):
    if dp[-1][1] <= arr[i][0]:
        dp.append(arr[i])
    if dp[-1][1] > arr[i][1]:
        dp[-1] = arr[i]
print(len(dp))