N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]
print("<", end="")
length = len(arr)
idx = 0
while len(arr) > 1:
    idx = (idx+K-1) % length
    print(arr[idx], end=", ")
    arr.pop(idx)
    length -= 1
print(arr[0], end=">")