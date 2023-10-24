dp = [1]
n = int(input())
for i in range(1,n+1):
    # f(n) = f(n-1)+f(n-2)
    if i > 0:
        dp.append(dp[i-1])
    if i > 1:
        dp[i] += dp[i-2]*2
    # overflow 때문에 % 연산
    # 다른 언어의 경우 메모리 한계로 dp에 저장할 때 마다 % 연산이 필요
    dp[i] %= 10007
print(dp[n])