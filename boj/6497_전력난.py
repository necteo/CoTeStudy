import sys
sys.setrecursionlimit(300000)

def find(u):
    if p[u] != u:
        p[u] = find(p[u])
    return p[u]

def union(u, v):
    r1 = find(u)
    r2 = find(v)
    p[r1] = p[r2]

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    p = [i for i in range(m)]
    arr = []
    total = 0
    for _ in range(n):
        a, b, c = map(int, input().split())
        arr.append([c, a, b])
        total += c
    arr.sort()
    sum = 0
    for w, u, v in arr:
        if find(u) != find(v):
            union(v, u)
            sum += w
    print(total - sum)
