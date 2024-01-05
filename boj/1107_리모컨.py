N = int(input())
M = int(input())
broken = list(map(int, input().split()))
ans = [max(N-100, 100-N)]
if N == 100:
    print(ans[0])
else:
    des = []
    while N != 0:
        des.append(N%10)
        N //= 10
    des.reverse()
    for
