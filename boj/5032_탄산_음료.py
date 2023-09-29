e,f,c = map(int, input().split())
ans = 0
t = e+f
while t >= c:
    ans += t//c
    t = t//c + t%c
print(ans)