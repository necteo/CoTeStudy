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
# 유클리드 호제법
def gcd(r1, r2):
    if r1 % r2 == 0:
        return r2
    return gcd(r2, r1%r2)

print(gcd(max(c, d), min(c, d)))

a, b = c, d
while c != d:
    if c < d:
        c += a
    elif d < c:
        d += b
print(c)