a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())
m = a*p
if p <= c:
    print(min(m, b))
else:
    print(min(m, b+(p-c)*d))