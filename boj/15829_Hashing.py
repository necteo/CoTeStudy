r = 31
M = 1234567891
L = int(input())
s = input()
ans = 0
n = 0
for i in s:
    ans += (ord(i)-ord('a')+1)*(r**n)
    n += 1
print(ans % M)
