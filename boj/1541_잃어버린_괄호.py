import sys
input = sys.stdin.readline
form = input()
nums = []
ops = []
idx = 0
for i in range(len(form)):
    if form[i] == '+' or form[i] == '-':
        nums.append(int(form[idx:i]))
        ops.append(form[i])
        idx = i+1
nums.append(int(form[idx:]))

sums = []
s = 0
for i in range(len(ops)):
    if ops[i] == '+':
        s += nums[i]
        if i == len(ops)-1:
            s += nums[i+1]
            sums.append(s)
    else:
        s += nums[i]
        sums.append(s)
        s = 0
        if i == len(ops)-1:
            sums.append(nums[-1])
if sums:
    ans = sums[0]
else:
    ans = nums[0]
for i in range(1, len(sums)):
    ans -= sums[i]
print(ans)