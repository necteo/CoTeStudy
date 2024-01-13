import sys
input = sys.stdin.readline
N, M = map(int, input().split())
dd = {}
for i in range(1, N+1):
    dd.setdefault(input().rstrip(), i)
bd = {}
for i in range(1, M+1):
    bd.setdefault(input().rstrip(), i)
ans = []
for k in dd.keys():
    if bd.get(k):
        ans.append(k)
ans.sort()
print(len(ans))
for i in ans:
    print(i)