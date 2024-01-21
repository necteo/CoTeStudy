import sys
input = sys.stdin.readline
M = int(input())
S = set()

def sets(c):
    if len(c) == 2:
        c[1] = int(c[1])
    if c[0] == "add":
        S.add(c[1])
    elif c[0] == "remove":
        if c[1] in S:
            S.remove(c[1])
    elif c[0] == "check":
        print(int(c[1] in S))
    elif c[0] == "toggle":
        if c[1] in S:
            S.remove(c[1])
        else:
            S.add(c[1])
    elif c[0] == "all":
        for i in range(1, 21):
            S.add(i)
    elif c[0] == "empty":
        S.clear()

for _ in range(M):
    cmd = list(input().split())
    sets(cmd)