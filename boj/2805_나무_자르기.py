N, M = map(int, input().split())
height = list(map(int, input().split()))
high = max(height)
low = 0
mid = high
while low+1 < high:
    total = 0
    for i in height:
        if i > mid:
            total += i-mid
    if total >= M:
        low = mid
        mid = (high+mid)//2
    else:
        high = mid
        mid = (mid+low)//2
