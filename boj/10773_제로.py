arr = []
for _ in range(int(input())):
    n = int(input())
    if n != 0:
        arr.append(n)
    else:
        arr.pop()
print(sum(arr))