V, E = map(int, input().split())
weights = []
for _ in range(E):
    a, b, c = map(int, input().split())
    weights.append([a, b, c])
weights.sort(key=lambda t: t[2])

p = []
for i in range(V+1):
    p.append(i)

def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]

def union(u, v):
    root1 = find(u)
    root2 = find(v)
    p[root1] = root2

mst_cost = 0
tree_edges = 0
for u, v, w in weights:
    if find(u) != find(v):
        union(u, v)
        tree_edges += 1
        mst_cost += w

print(mst_cost)