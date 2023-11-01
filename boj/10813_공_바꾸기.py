n,m = map(int, input().split())
b = [i for i in range(1,n+1)]
for _ in range(m):
    i,j = map(int, input().split())
    i -= 1
    j -= 1
    b[i], b[j] = b[j], b[i]
print(*b)