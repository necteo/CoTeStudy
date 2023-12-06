n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
stack = []
idx = 1
cur = 0
ans = []
while cur != n:
    if idx <= arr[cur]:
        stack.append(idx)
        ans.append('+')
        idx += 1
        continue
    v = stack.pop()
    if v == arr[cur]:
        ans.append('-')
        cur += 1
    else:
        ans = []
        break

if not ans:
    print("NO")
else:
    for i in ans:
        print(i)