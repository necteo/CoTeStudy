n = int(input())
a, pa, b, pb = map(int, input().split())
ans = [0, 0, 0]
for i in range(n//pa+1, -1, -1):
    for j in range(n//pb+1):
        s = a*i + b*j
        if pa*i + pb*j <= n:
            if s > ans[0]:
                ans = [s, i, j]
print(ans[1], ans[2])

16 2 4

a:8 b:0 0//4
a:7 b:0 2//4
a:6 b:1 4//4
a:5 b:1 6//4
a:4 b:2 8//4

a:0 b:4 0//2
a:2 b:3 4//2
a:4 b:2
a:6 b:1
a:8 b:0