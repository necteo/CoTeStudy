# readlines_test.py

f = open("C:/Users/USER/Documents/py/새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    line = line.strip()
    print(line)
f.close()
