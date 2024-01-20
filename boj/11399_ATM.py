N = int(input())
P = list(map(int, input().split()))
P.sort()
k = 0
ans = 0
for t in P:
    k += t
    ans += k
print(ans)