n = int(input())
p = [i for i in range(n+1)]

def find(u):
    if p[u] != u:
        p[u] = find(p[u])
    return p[u]

def union(u, v):
    r1 = find(u)
    r2 = find(v)
    p[r1] = p[r2]

for _ in range(n-1):
    a,b = map(int, input().split())
    if b == 1 or find(b) == 1:
        union(a,b)
    else:
        union(b,a)

for i in range(2,n+1):
    print(p[i])