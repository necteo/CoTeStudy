import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr_sum = [0]
for i in range(1, n+1):
    arr_sum.append(arr_sum[i-1] + arr[i-1])
for _ in range(m):
    i, j = map(int, input().split())
    print(arr_sum[j]-arr_sum[i-1])