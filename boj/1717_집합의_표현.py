import sys
sys.setrecursionlimit(100000)

n,m = map(int, input().split())

p = []
for i in range(n+1):
    p.append(i)

def find(u):
    if u == p[u]:
        return u
    p[u] = find(p[u])
    return p[u]

def union(x, y):
    p[find(x)]=find(y)

for i in range(m):
    op,a,b=map(int, input().split())
    if op == 0:
        union(a,b)
    elif op == 1:
        if find(a) == find(b):
            print('yes')
        else:
            print('no')
