import sys
input = sys.stdin.readline

def find(u):
    if u == p[u]:
        return u
    p[u] = find(p[u])
    return p[u]

def union(x, y):
    u = find(x)
    v = find(y)
    if u != v:  # 이미 같은 부모인 경우 반대로 입력하면 부모의 자식 개수가 0이 되기 때문에
        p[v] = u
        cnt[u] += cnt[v]
        cnt[v] = 0

for _ in range(int(input())):
    dic = {}    # dic이 arr보다 빠름
    pid = 0
    p = []
    cnt = []    # 부모의 자식 개수를 일일이 찾으면 O(n)이기 때문에 O(1)에 찾는 리스트에 저장
    F = int(input())
    for _ in range(F):
        a, b = input().split()
        if a not in dic:
            dic[a] = pid
            p.append(pid)
            pid += 1
            cnt.append(1)
        if b not in dic:
            dic[b] = pid
            p.append(pid)
            pid += 1
            cnt.append(1)
        c = find(dic.get(a))
        union(c, dic.get(b))
        print(cnt[c])