import sys
sys.setrecursionlimit(100000)
n = int(input())
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
visit = [0] * (n+1)
tree = [[1, 1]] * (n+1)

def dfs(i):
    visit[i] = 1
    for u in g[i]:
        if visit[u] == 0:
            tree[u] = [i, tree[i][1]+1]
            dfs(u)
dfs(1)

def LCA(a, b):
    while tree[a][1] != tree[b][1]:
        if tree[a][1] > tree[b][1]:
            a = tree[a][0]
        else:
            b = tree[b][0]
    while a != b:
        a = tree[a][0]
        b = tree[b][0]
    return a


for _ in range(int(input())):
    a, b = map(int, input().split())
    print(LCA(a, b))
