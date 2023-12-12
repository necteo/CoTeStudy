a, b = map(int, input().split())
c, d = a, b
x = 1
y = 0
while x != y:
    y = x
    for i in range(2, min(a, b)+1):
        if a % i == 0 and b % i == 0:
            a //= i
            b //= i
            x *= i
            break
print(x)
a, b = c, d
while c != d:
    if c < d:
        c += a
    elif d < c:
        d += b
print(c)