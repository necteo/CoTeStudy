import sys
input = sys.stdin.readline
N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))
ans = [0, 0]

def solve(a, b, n):
    blue = 0
    for i in range(n):
        for j in range(n):
            if paper[b+i][a+j] == 1:
                blue += 1
    if blue == n*n:
        ans[1] += 1
    elif blue == 0:
        ans[0] += 1
    else:
        solve(a, b, n//2)
        solve(a+n//2, b, n//2)
        solve(a, b+n//2, n//2)
        solve(a+n//2, b+n//2, n//2)

solve(0, 0, N)
print(ans[0])
print(ans[1])