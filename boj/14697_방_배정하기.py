def room():
    a,b,c,n = map(int, input().split())
    m=n//a+1
    s = 0
    for i in range(m):
        for j in range(m):
            for k in range(m):
                s = a*i + b*j + c*k
                if s == n:
                    print(1)
                    return
    print(0)

room()