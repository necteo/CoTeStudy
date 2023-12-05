n = int(input())
while n != 0:
    arr = []
    while n > 0:
        arr.append(n % 10)
        n //= 10
    l = len(arr)
    cnt = 0
    for i in range(l // 2):
        if arr[i] == arr[l - i - 1]:
            cnt += 1
    if cnt == l // 2:
        print('yes')
    else:
        print('no')
    n = int(input())
