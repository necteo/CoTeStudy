# ab.py

f = input()
a = int(f.split()[0])
b = int(f.split()[1])

if a >= 1 and a <= 10000 and b >= 1 and b <= 10000:
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a % b)
