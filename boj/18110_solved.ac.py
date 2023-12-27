import sys
input = sys.stdin.readline
n = int(input())
arr = []
if n == 0:
    print(0)
else:
    for i in range(n):
        arr.append(int(input()))
    arr.sort()
    x = round(n*0.15+1e-9)  # EPS
    m = sum(arr[x:n-x])/(n-2*x)+1e-9
    print(round(m))