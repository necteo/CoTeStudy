import sys
n = int(sys.stdin.readline())
list = []
for _ in range(n):
    list.append(int(sys.stdin.readline()))
for i in range(n, 0, -1):
    for j in range(i - 1):
        if list[j] > list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]
for i in range(n):
    print(list[i])
