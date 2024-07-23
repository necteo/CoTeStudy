import sys
input = sys.stdin.readline

n = int(input())
triangle = []
dp = []
for i in range(n):
    triangle.append(list(map(int, input().split())))
    dp.append([0 for _ in range(i)])

for i in range(n-1, 0, -1):
    for j in range(n-1):
        dp[i-1][j] = triangle[i-1][j] + max(triangle[i][j], triangle[i][j+1])
