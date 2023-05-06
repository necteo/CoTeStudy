# adddata.py

f = open("C:/Users/USER/Documents/py/새파일.txt", 'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# with open("C:/Users/USER/Documents/py/새파일.txt", 'a') as f:
#     for i in range(11, 20):
#         data = "%d번째 줄입니다.\n" % i
#         f.write(data)
