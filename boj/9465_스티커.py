import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = []
    for _ in range(2):
        s.append([0]+list(map(int, input().split())))
    dp = [-1 for _ in range(n+1)]
    dp[0] = 0
    sum = 0

    for i in range(n):
        a = sum+s[dp[i]][i]+s[(dp[i]+1)%2][i+1]
        b = sum+s[dp[i]][i+1]
        c = sum-s[dp[i-1]][i-1]+s[(dp[i]+1)%2][i]+s[dp[i]][i+1]
        
        if a >= b and a >= c:
            sum += s[dp[i]][i]
            dp[i+1] = (dp[i]+1)%2
        elif b >= a and b >= c:
            dp[i+1] = dp[i]
            dp[i] = -1
        elif c >= a and c >= b:
            sum = sum-s[dp[i-1]][i-1]+s[(dp[i]+1)%2][i]
            dp[i+1] = dp[i]
            dp[i] = (dp[i]+1)%2
            dp[i-1] = -1
        print(dp, sum)
        
    sum += s[dp[-1]][-1]
    print(sum)
