import sys
input = sys.stdin.readline

n = int(input())
triangle = []

for i in range(n):
    triangle.append(list(map(int, input().split())))

for i in range(n-1, 0, -1):
    for j in range(i):
        triangle[i-1][j] = triangle[i-1][j] + max(triangle[i][j], triangle[i][j+1])
        
print(*triangle[0])