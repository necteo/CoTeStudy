import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = []
    dp = []
    for _ in range(2):
        s.append(list(map(int, input().split())))
        dp.append([0 for _ in range(n)])

    dp[0][0] = s[0][0]
    dp[1][0] = s[1][0]

    for i in range(1, n):
        a = s[0][i]+dp[1][i-1]
        b = s[0][i]+dp[1][i-2]  # if i==1: dp[-1] == 0
        c = s[1][i]+dp[0][i-1]
        d = s[1][i]+dp[0][i-2]

        if a >= b:
            dp[0][i] = a
        else:
            dp[0][i] = b
        if c >= d:
            dp[1][i] = c
        else:
            dp[1][i] = d
    print(max(max(dp[0]), max(dp[1])))
