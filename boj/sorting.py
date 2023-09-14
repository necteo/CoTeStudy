def qs(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    left=[]
    right=[]
    for i in range(1,len(arr)):
        if arr[i]<=pivot:    
            left.append(arr[i])
        else:
            right.append(arr[i])
    left=qs(left)
    right=qs(right)
    return left+[pivot]+right

arr=[int(input()) for i in range(int(input()))]
arr=qs(arr)
for i in arr:
    print(i)
