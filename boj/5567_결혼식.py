from collections import deque
V=int(input())+1
E=int(input())
arr=[[] for _ in range(V+1)]
for _ in range(E):
    a,b=map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
visited=[0 for _ in range(V+1)]
def bfs(start):
    visited[start]=1
    queue=deque()
    queue.append(start)
    while len(queue)!=0:
        v=queue.popleft()
        for i in arr[v]:
            if visited[i]==0:
                visited[i]=visited[v]+1 #visited가 깊이를 나타냄
                queue.append(i)

bfs(1)
cnt=0
for i in range(2,V+1):
    if visited[i] < 4 and visited[i] != 0:
        cnt += 1
print(cnt)
