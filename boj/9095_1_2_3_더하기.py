dp = [1]
for _ in range(int(input())):
    n = int(input())
    for i in range(1, n+1):
        if len(dp) > i:
            continue
        # 점화식은 f(n) = f(n-1)+f(n-2)+f(n-3)
        if i > 0:
            dp.append(dp[i-1])
        if i > 1:
            dp[i] += dp[i-2]
        if i > 2:
            dp[i] += dp[i-3]
    print(dp[n])