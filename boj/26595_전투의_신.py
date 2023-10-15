n = int(input())
a, pa, b, pb = map(int, input().split())
ans = [0, 0, 0]
for i in range(n+1):
    x = i//pa if i != 0 else 0
    y = (n-i)//pb if i != n else 0
    s = a*x + b*y
    if pa*x + pb*y <= n:
        if s > ans[0]:
            ans = [s, x, y]
print(ans[1], ans[2])