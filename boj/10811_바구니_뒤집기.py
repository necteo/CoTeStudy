n,m = map(int, input().split())
basket = [i for i in range(1,n+1)]
for _ in range(m):
    i,j = map(int, input().split())
    for k in range(i-1, i+(j-i)//2):
        basket[k], basket[j-1-k] = basket[j-1-k], basket[k]
print(*basket)