import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
broken = []
if M > 0:
    broken = list(map(int, input().split()))
ans = [max(N-100, 100-N)]

for i in range(1000001):
    des = []
    k = i
    while i != 0:
        des.append(i%10)
        i //= 10
    if not des:
        des = [0]
    chk = True
    for j in des:
        if j in broken:
            chk = False
    if chk:
        ans.append(max(k-N, N-k)+len(des))

ans.sort()
print(ans[0])