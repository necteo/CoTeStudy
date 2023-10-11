m1, m2 = input().split('+')
m2, m3 = m2.split('=')

def countAtom(f):
    atom_cnt = [0,0,0]
    for i in range(len(f)):
        if f[i] == 'C':
            atom_cnt[0] += 1
        elif f[i] == 'H':
            atom_cnt[1] += 1
        elif f[i] == 'O':
            atom_cnt[2] += 1
        else:
            if f[i-1] == 'C':
                atom_cnt[0] += int(f[i])-1
            elif f[i-1] == 'H':
                atom_cnt[1] += int(f[i])-1
            elif f[i-1] == 'O':
                atom_cnt[2] += int(f[i])-1
    return atom_cnt

n1 = countAtom(m1)
n2 = countAtom(m2)
n3 = countAtom(m3)
arr = []
for i in range(1, 11):
    l3 = list(map(lambda x: x * i, n3))
    for j in range(1, 11):
        l2 = list(map(lambda x: x * j, n2))
        for k in range(1, 11):
            l1 = list(map(lambda x: x * k, n1))
            if list(map(lambda a,b: a+b, l1, l2)) == l3:
                arr.append([k, j, i])
arr.sort()
print(*arr[0])