A, B = map(int, input().split())
ans = 10**9


def AtoB(cnt):
    global ans, A, B
    if A == B:
        ans = min(ans, cnt)
        return
    if A > B:
        return
    A *= 2
    AtoB(cnt+1)
    A //= 2
    A = A*10+1
    AtoB(cnt+1)
    A //= 10


AtoB(1)
if ans == 10**9:
    print(-1)
else:
    print(ans)
