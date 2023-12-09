import sys
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()
print(round(sum(arr)/N))
print(arr[N//2])
idx = 0
cnt = [[arr[idx], 1]]
for i in range(1, N):
    if arr[i] > arr[i-1]:
        idx += 1
        cnt.append([arr[i], 0])
    cnt[idx][1] += 1
cnt.sort(key=lambda x: x[1], reverse=True)
if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])
print(arr[-1]-arr[0])