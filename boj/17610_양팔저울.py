def subSet(right, left, depth):
    if depth == k:
        ans.discard(abs(right - left))
        return
    subSet(right+arr[depth], left, depth+1)
    subSet(right, left+arr[depth], depth+1)
    subSet(right, left, depth+1)


k = int(input())
arr = list(map(int, input().split()))
ans = set()
for i in range(1, sum(arr)+1):
    ans.add(i)
subSet(0, 0, 0)
print(len(ans))