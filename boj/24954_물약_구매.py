import sys
input = sys.stdin.readline
n = int(input())
c = list(map(int, input().split()))
p = []
for _ in range(n):
    pi = int(input())
    info = []
    for _ in range(pi):
        a,d = map(int, input().split())
        info.append([a,d])
    p.append(info)

check = [0 for _ in range(n)]
tmp = []
coin = 0
min_coin = 1000000

def potion(idx):
    global coin, min_coin
    if idx == n:
        min_coin = min(min_coin, coin)
        return
    for i in range(n):
        if check[i] == 0:
            check[i] = 1
            for aj,dj in p[i]:
                c[aj-1] -= dj
            tmp.append(i)
            coin = coin+c[i] if c[i] > 0 else coin+1
            potion(idx+1)
            coin = coin-c[i] if c[i] > 0 else coin-1
            tmp.pop()
            for aj,dj in p[i]:
                c[aj-1] += dj
            check[i] = 0

potion(0)
print(min_coin)