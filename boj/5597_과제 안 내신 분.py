p = set([i for i in range(30)])
for _ in range(28):
    n = int(input())
    p.remove(n-1)
list(p).sort()
for i in p:
    print(i+1)