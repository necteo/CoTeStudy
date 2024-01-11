import sys
input = sys.stdin.readline
N, M = map(int, input().split())
dic = []
for i in range(1, N+1):
    dic.append(input().rstrip())
for _ in range(M):
    q = input().rstrip()
    if ord('1') <= ord(q[0]) <= ord('9'):
        print(dic[int(q)-1])
    else:
        print(dic.index(q)+1)