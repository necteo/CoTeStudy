import sys
input = sys.stdin.readline
n,s = map(int, input().split())
arr = list(map(int, input().split()))
ans = []

def select(sub, dep):
    if dep == n-1:
        if sub and sum(sub) == s:
            ans.append(sub)
        return
    select(sub, dep+1)
    sub.append(arr[dep+1])
    select(sub, dep+1)
    if sub:
        sub.pop()

select([], -1)
print(len(ans))
