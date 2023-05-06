# nameoji.py

f = input()
a = int(f.split()[0])
b = int(f.split()[1])
c = int(f.split()[2])

if a >= 2 and a <= 10000 and b >= 2 and b <= 10000 and c >= 2 and c <= 10000:
    print((a + b) % c)
    print(((a % c) + (b % c)) % c)
    print(a * b % c)
    print(((a % c) * (b % c)) % c)
