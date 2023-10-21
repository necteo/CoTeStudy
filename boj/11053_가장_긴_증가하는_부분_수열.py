n = int(input())
A = list(map(int, input().split()))
dp = [1 for _ in range(n)]

# n^2으로 해결 하는 방법
for i in range(1, n):
    val = 0
    for j in range(i):
        if A[j] < A[i]:
            if val < dp[j]:
                val = dp[j]
    dp[i] = val+1
cnt = 0
for i in dp:
    if cnt < i:
        cnt = i
print(cnt)