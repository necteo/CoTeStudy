x=''
for i in input():
    a=int(i)
    for j in range(2,-1,-1):
        x+=str(a//(2**j))
        a%=(2**j)
print(int(x))
