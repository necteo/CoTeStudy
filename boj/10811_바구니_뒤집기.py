n,m = map(int, input().split())
basket = [i for i in range(1,n+1)]
for _ in range(m):
    i,j = map(int, input().split())
    for k in range((j-i)//2+1):
        basket[i-1+k], basket[j-1-k] = basket[j-1-k], basket[i-1+k]
print(*basket)