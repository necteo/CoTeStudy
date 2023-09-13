n, m = map(int, input().split())
arr = [i for i in range(n, m+1)]
prime = [2, 3]

if arr[0] == 1:
    arr[0] = 0
for i in range(2, int(m**0.5)+1):
    p = 1
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            p = 0
            break
        if p:
            prime.append(j)
for i in range(len(arr)):
    for j in prime:
        if arr[i] == 0:
            break
        if arr[i] == j:
            print(arr[i])
        elif arr[i] % j == 0:
            arr[i] = 0
            break
