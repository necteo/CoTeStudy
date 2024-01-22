import sys
import heapq
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

def dij():
