N = int(input())
arr = list(map(int, input().split()))
d = {}
for i in arr:
    if i in d:
        d[i] += 1
    else:
        d.setdefault(i, 1)
M = int(input())
arr2 = list(map(int, input().split()))
for i in arr2:
    if i in d:
        print(d[i], end=" ")
    else:
        print(0, end=" ")