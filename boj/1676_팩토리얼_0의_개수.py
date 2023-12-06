n = int(input())
for i in range(2, n):
    n *= i
cnt = 0
if n > 0:
    while n % 10 == 0:
        cnt += 1
        n //= 10
print(cnt)