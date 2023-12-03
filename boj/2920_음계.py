scale = list(map(int, input().split()))
res = 0
for i in range(4):
    if scale[i] < scale[7-i]:
        res += 1
    else:
        res -= 1
if res == 4:
    print("ascending")
elif res == -4:
    print("descending")
else:
    print("mixed")