import sys
input = sys.stdin.readline
n,m = map(int, input().split())
prefer = []
for _ in range(n):
    prefer.append(list(map(int, input().split())))
chicken = []
people = [0 for _ in range(n)]
maxp = 0

def sel(idx):
    if len(chicken) == 3:
        global maxp
        for i in range(n):
            people[i] = max(prefer[i][chicken[0]], prefer[i][chicken[1]], prefer[i][chicken[2]])
        maxp = max(maxp, sum(people))
        return
    if idx == m:
        return
    chicken.append(idx)
    sel(idx+1)
    chicken.pop()
    sel(idx+1)

sel(0)
print(maxp)