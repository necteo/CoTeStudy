N, K = map(int, input().split())
ans = 1
for _ in range(K):
    ans *= N
    N -= 1
for i in range(K, 0, -1):
    ans //= i
print(ans)