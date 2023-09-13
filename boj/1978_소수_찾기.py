input()
num = list(map(int, input().split()))
cnt = 0
for i in num:
    prime = 1
    if i == 1:
        prime = 0
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            prime = 0
            break
    cnt += prime
print(cnt)