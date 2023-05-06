# a_min_b.py

f = input()
a = int(f.split()[0])
b = int(f.split()[1])

if a > 0 and a < 10 and b > 0 and b < 10:
    print(a - b)
else:
    print("조건: 0 < a, b < 10")
