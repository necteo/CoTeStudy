n = int(input())
a, pa, b, pb = map(int, input().split())
ans = [0, 0, 0]
for i in range(n//pa, -1, -1):
    j = n%i//pb if i != 0 else n//pb
    s = a*i + b*j
    if pa*i + pb*j <= n:
        if s > ans[0]:
            ans = [s, i, j]
print(ans[1], ans[2])