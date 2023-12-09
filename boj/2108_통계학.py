import sys
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()
print(round(sum(arr)/N))
print(arr[N//2])
cnt = []
for i in range(N):

print(arr[-1]-arr[0])