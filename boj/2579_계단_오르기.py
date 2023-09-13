n = int(input())
score = [0]
for _ in range(n):
    score.append(int(input()))
maxn = 0
if n == 1:
    maxn = score[1]
elif n == 2:
    maxn = score[1] + score[2]
else:
    sum = [score[0], score[1], score[1]+score[2]]
    for i in range(3, n+1):
        sum.append(max(sum[i-2] + score[i], sum[i-3] + score[i-1] + score[i]))
    maxn = sum[-1]
print(maxn)