import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = []
p = [i for i in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    arr.append([c,a,b])
arr.sort()

def find(u):
    if u == p[u]:
        return u
    p[u] = find(p[u])
    return p[u]

def union(x, y):
    p[find(y)] = find(x)

sum = 0
for w,u,v in arr:
    if find(u) != find(v):
        union(u,v)
        sum += w
print(sum)