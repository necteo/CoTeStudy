N, r, c = map(int, input().split())
a = 0
b = 2**(2*N)-1
x, y = 0, 0
l = 2**N-1

while a != b:
    if r < y+l//2+1:
        if c > x+l//2:
            a = a+4**(N-1)
            x = x+l//2+1
    else:
        if c < x+l//2+1:
            a = a+4**(N-1)*2
        else:
            a = a+4**(N-1)*3
            x = x+l//2+1
        y = y+l//2+1
    b = a+4**(N-1)-1
    N -= 1
    l //= 2
print(a)