N, r, c = map(int, input().split())
a = 0
b = 2**(2*N)-1
l = 2**N-1

while a != b:
    if r < l//2+1:
        if c < l//2+1:
            b = b//4-1
