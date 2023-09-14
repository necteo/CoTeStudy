from collections import deque

V,E = map(int,input().split())
#인접리스트
arr=[[] for _ in range(V+1)]
for i in range(E):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [0 for _ in range(V+1)]

def BFS(start):
    queue = deque()
    queue.append(start)
    visited[start]=1
    while len(queue)!=0:
        v = queue.popleft()
        for i in arr[v]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)

cnt = 0
for i in range(1,V+1):
    if visited[i] == 0:
        cnt += 1
        BFS(i)

print(cnt)
