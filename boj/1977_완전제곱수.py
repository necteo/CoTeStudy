import math

m = int(input())
n = int(input())
sum = 0
for i in range(math.ceil(m**0.5), math.floor(n**0.5)+1):
    sum += i*i
if sum != 0:
    print(sum)
    print(math.ceil(m**0.5)**2)
else:
    print(-1)