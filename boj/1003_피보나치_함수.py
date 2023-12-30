import sys
input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    zero = [1, 0]
    one = [0, 1]
    for i in range(2, N+1):
        zero.append(zero[i-1]+zero[i-2])
        one.append(one[i-1]+one[i-2])
    print(zero[N], one[N])