import sys
input = sys.stdin.readline
N = int(input())
minh = [0]

def insert(x):
    minh.append(x)
    idx = len(minh)-1
    while minh[idx] < minh[idx//2]:
        tmp = minh[idx//2]
        minh[idx//2] = minh[idx]
        minh[idx] = tmp
        idx //= 2

def pop():
    if minh[-1] == 0:
        return 0
    else:
        res = minh[1]
        minh[1] = minh[-1]
        minh.pop()
        p = 1
        while True:
            c = p*2
            if len(minh) > c+1 and minh[c] > minh[c+1]:
                c += 1
            if c >= len(minh) or minh[c] > minh[p]:
                break
            tmp = minh[c]
            minh[c] = minh[p]
            minh[p] = tmp
            p = c
        return res

for _ in range(N):
    x = int(input())
    if x == 0:
        print(pop())
    else:
        insert(x)