from collections import deque
V=int(input())
E=int(input())
arr=[[] for _ in range(V+1)]
for _ in range(E):
    a,b=map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

def bfs(start):
    visited=[0 for _ in range(V+1)]
    visited[start]=1
    queue=deque()
    queue.append(start)
    cnt=0
    while len(queue)!=0:
        v=queue.popleft()
        for i in arr[v]:
            if visited[i]==0:
                visited[i]=1
                queue.append(i)
                cnt+=1
    return cnt

print(bfs(1))
