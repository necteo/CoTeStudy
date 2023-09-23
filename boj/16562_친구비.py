import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
A = [0] + list(map(int, input().split()))
p = [i for i in range(n+1)]
chk = [0 for i in range(n+1)]

def find(u):
    if p[u] == u:
        return u
    p[u] = find(p[u])
    return p[u]

def union(u1, u2):
    p[u1] = u2

for _ in range(m):
    v, w = map(int, input().split())
    v = find(v)
    w = find(w)
    if A[v] < A[w]:
        union(w, v)
    else:
        union(v, w)
sum = 0
for i in range(1, n+1):
    x = p[find(i)]  # 관계를 추가할 때 나중에 최소 비용 부모가 추가 될 수 있어서 여기서 한번 더 최소 비용 부모를 찾아야 함
    if chk[x] == 0:
        k -= A[x]
        sum += A[x]
        chk[x] = 1

if k >= 0:
    print(sum)
else:
    print("Oh no")