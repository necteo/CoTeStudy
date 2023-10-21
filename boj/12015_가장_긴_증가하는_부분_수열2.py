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


# nlogn으로 해결 하는 방법 (부분 수열의 길이만 구할 수 있다)
end = 0
for i in range(1, n):
    if arr[-1] < A[i]:
        arr.append(A[i])
        end += 1
    else:
        idx = lower_bound(0, end, A[i])
        arr[idx] = A[i]
print(len(arr))