n,d = map(int, input().split())
ori = 0
for k in range(d-1,-1,-1):
    if k == 1:
        continue
    if k == 0:
        ori += 1*d**(d-1)
    else:
        ori += k*d**(d-1-k)
ori = max(n, ori-1)
nf = 0
while nf == 0:
    check = [0 for _ in range(d)]
    num = 0
    ori += 1
    n = ori
    i = 0
    while n > 0:
        if check[n%d] == 0:
            check[n%d] = 1
            num += n%d*(10**i)
            n //= d
            i += 1
        else:
            if 0 not in check:
                nf = -1
            break
        if 0 not in check:
            nf = 1

if nf == -1:
    print(-1)
else:
    print(ori)