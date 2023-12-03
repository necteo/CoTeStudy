scale = list(map(int, input().split()))
res = 0
for i in range(7):
    if scale[i] < scale[i+1]:
        res += 1
    else:
        res -= 1
if res == 7:
    print("ascending")
elif res == -7:
    print("descending")
else:
    print("mixed")