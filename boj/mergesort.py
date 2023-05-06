import sys

def merge(data, left, mid, right):
    sorted_list = [0] * len(data)
    l_idx = left
    r_idx = mid + 1
    cur = left

    while l_idx <= mid and r_idx <= right:
        if data[l_idx][0] < data[r_idx][0]:
            sorted_list[cur] = data[l_idx]
            l_idx += 1
        elif data[l_idx][0] == data[r_idx][0] and data[l_idx][1] < data[r_idx][1]:
            sorted_list[cur] = data[l_idx]
            l_idx += 1 
        else:
            sorted_list[cur] = data[r_idx]
            r_idx += 1
        cur += 1

    while l_idx <= mid:
        sorted_list[cur] = data[l_idx]
        l_idx += 1
        cur += 1

    for i in range(left, cur):
        data[i] = sorted_list[i]

def merge_sort(data, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(data, left, mid)
        merge_sort(data, mid + 1, right)
        merge(data, left, mid, right)

n = int(sys.stdin.readline())
data = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    data.append([x, y])
    
merge_sort(data, 0, len(data) - 1)
for xy in data:
    print(*xy)