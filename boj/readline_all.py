# readline_all.py

f = open("C:/Users/USER/Documents/py/새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()
