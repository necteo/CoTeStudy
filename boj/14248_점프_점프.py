from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
stones = [0] + list(map(int, input().split()))
s = int(input())
visited = [0 for _ in range(n+1)]

def bfs(start):
    queue = deque()
    queue.append(start)
    while queue:
        v = queue.popleft()
        if visited[v] == 0:
            visited[v] = 1
            u = stones[v]
            if v-u > 0:
                queue.append(v-u)
            if v+u <= n:
                queue.append(v+u)

bfs(s)
print(visited.count(1))