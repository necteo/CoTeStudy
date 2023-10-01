arr = []
for _ in range(9):
    arr.append(int(input()))
arr.sort()
s = 0
x,y = 0,0
for i in range(9):
    for j in range(i+1,9):
        for k in range(9):
            if k != i and k != j:
                s += arr[k]
        if s == 100:
            for n in range(9):
                if n != i and n != j:
                    print(arr[n])
            break
        s = 0
    if s == 100:
        break