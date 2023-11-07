s = input()
chk = 1
n = len(s)
for i in range(n//2):
    if s[i] != s[n-i-1]:
        chk = 0
print(chk)