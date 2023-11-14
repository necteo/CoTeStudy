N = int(input())
money = list(map(int, input().split()))
M = int(input())
high = max(money)
low = min(money)
mid = high
total = 0
while total > M:
    total = 0
    for i in money:
        if i > mid:
            total += mid
        else:
            total += i