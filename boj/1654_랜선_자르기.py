K, N = map(int, input().split())
arr = []
for _ in range(K):
    arr.append(int(input()))
high = sum(arr)//N
low = 0
mid = high
while low+1 < high:
    cnt = 0
    for i in arr:
        cnt += i//mid
    if cnt < N:
        high = mid
        mid = (mid+low)//2
    else:
        low = mid
        mid = (high+mid)//2
print(mid)