import sys
input = sys.stdin.readline
N = int(input())
home = []
for _ in range(N):
    home.append(list(map(int, input().split())))
ans = [home[0]]
for i in range(1, N):
    ans.append([sys.maxsize, sys.maxsize, sys.maxsize])
    for j in range(3):
        for k in range(3):
            if j != k:
                ans[i][k] = min(ans[i][k], ans[i-1][j]+home[i][k])
print(min(ans[-1]))