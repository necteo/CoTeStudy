for _ in range(int(input())):
    n, m = map(int, input().split())
    xl = list(map(int, input().split()))
    yl = list(map(int, input().split()))
    plate = list(map(int, input().split()))
    x,y = 0,0
    cnt = 0
    for i,j in zip(xl,yl):
        m -=1
        x += i*10**m
        y += j*10**m
    for i in range(n):
        z = 0
        m = len(xl)
        j = i
        while m >= 0:
            m -= 1
            z += plate[j]*10**m
            if j >= n-1:
                j = j-n
            else:
                j += 1
        print(z)