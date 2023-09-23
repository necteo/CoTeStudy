import sys
input = sys.stdin.readline
n,m = map(int, input().split())
p = [i for i in range(n)]

def find(u):
    if p[u] == u:
        return u
    p[u] = find(p[u])
    return p[u]

def union(x,y):
    p[find(x)] = find(y)

chk = 0
for i in range(m):
    a,b = map(int, input().split())
    if a < b:
        union(b,a)
    else:
        union(a,b)

if chk == 0:
    print(0)