N, K = map(int, input().split())
t = 0
while N != K:
    if K >= N*2:
        N *= 2
    elif N < K:
        N += 1
        t += 1
    elif N > K:
        N -= 1
        t += 1
print(t)