import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
arr = [A[0]]


def lower_bound(left, right, val):
    while left < right:
        mid = (left + right) // 2
        if val <= arr[mid]:
            right = mid
        else:
            left = mid+1
    return right


# nlogn으로 해결 하는 방법
index = [1]
end = 0
for i in range(1, n):
    if arr[-1] < A[i]:
        arr.append(A[i])
        end += 1
        index.append(end+1)
    else:
        idx = lower_bound(0, end, A[i])
        arr[idx] = A[i]
        index.append(idx+1)
t = len(arr)
print(t)
ans = []
# arr의 맨 뒤에서 부터 길이-1을 하면서 처음 만나는 원소가 부분 수열의 원소
for i in range(n-1, -1, -1):
    if t == index[i]:
        ans.append(A[i])
        t -= 1
for i in range(len(ans)-1, -1, -1):
    print(ans[i], end=" ")