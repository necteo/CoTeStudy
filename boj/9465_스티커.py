for _ in range(int(input())):
    n = int(input)
    sticker = []
    for _ in range(2):
        sticker.append(list(map(int, input().split())))
    dp = [-1 for _ in range(n)]
    sum = 0

    

    # if sticker[0][0]+max(sticker[1][1]+sticker[0][2], sticker[1][2]) < sticker[1][0]+max(sticker[0][1]+sticker[1][2], sticker[0][2]):
    #     dp[0] = 1
    #     if sticker[0][1]+sticker[1][2]< sticker[0][2]:
    #         dp[2] = 0
    #     else:
    #         dp[1] = 0
    # else:
    #     dp[0] = 0
    #     if sticker[1][1]+sticker[0][2] < sticker[1][2]:
    #         dp[2] = 1
    #     else:
    #         dp[1] = 1

    # i = 1
    # while i < n-2:
    #     if dp[i] == -1:
    #         continue
    #     if sticker[(dp[i]+1)%2][i+1]+sticker[dp[i]][i+2] < sticker[(dp[i]+1)%2][i+2]:
    #         dp[i+1] = i+1
    #         i+=1
    #     else:
    #         dp[i+2] = (dp[i]+1)%2
    #         i+=2

    # if dp[i] == -1:
    #     if sticker[(dp[i]+1)%2][i+1]+sticker[dp[i]][i+2] < sticker[(dp[i]+1)%2][i+2]:
    #         dp[i+1] = i+1
    #         i+=1
    #     else:
    #         dp[i+2] = (dp[i]+1)%2
    #         i+=2