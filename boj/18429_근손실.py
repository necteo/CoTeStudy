n,k = map(int, input().split())
kit = list(map(int, input().split()))
check = [0 for _ in range(n)]
tmp = []
ans = []
weight = 500

def perm(idx):
    global weight
    if idx == n:
        ans.append(tmp.copy())
        return
    weight -= k
    for i in range(n):
        if not check[i]:
            if weight+kit[i] < 500:
                continue
            check[i] = 1
            tmp.append(kit[i])
            weight += kit[i]
            perm(idx+1)
            tmp.pop()
            weight -= kit[i]
            check[i] = 0
    weight += k

perm(0)
print(len(ans))