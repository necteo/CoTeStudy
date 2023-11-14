N = int(input())
money = list(map(int, input().split()))
M = int(input())
high = max(money)
low = 0
mid = high
while low+1 < high:
    total = 0
    for i in money:
        if i > mid:
            total += mid
        else:
            total += i
    if total > M:
        high = mid
        mid = (mid+low)//2
    else:
        low = mid
        mid = (mid+high)//2
print(mid)