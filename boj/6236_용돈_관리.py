n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
low = max(arr)
high = sum(arr)
ans = 0


def chk(mid):
    money = 0
    cnt = 0
    for i in arr:
        if i > money or i < money and n-m == m-cnt:
            money = mid
            cnt += 1
        money -= i
    return cnt


while low <= high:
    mid = (low + high) // 2
    cnt = chk(mid)
    if cnt > m:
        low = mid + 1
    elif cnt <= m:
        high = mid - 1
        ans = mid

print(ans)