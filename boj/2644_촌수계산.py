from collections import deque
n = int(input())
a, b = map(int, input().split())
m = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

def bfs(p1, p2):
    visit = [0 for _ in range(n+1)]
    visit[p1] = 1
    queue = deque()
    queue.append(p1)
    cnt = 1
    while len(queue) != 0:
        for _ in range(len(queue)):
            v = queue.popleft()
            for i in arr[v]:
                if visit[i] == 0:
                    if i == p2:
                        return cnt
                    visit[i] = 1
                    queue.append(i)
        cnt += 1
    return -1

print(bfs(a, b))
