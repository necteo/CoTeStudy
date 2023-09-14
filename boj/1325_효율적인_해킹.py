import sys
from collections import deque
input = sys.stdin.readline

V,E=map(int,input().split())
arr=[[] for _ in range(V+1)]
for _ in range(E):
    a,b=map(int,input().split())
    arr[b].append(a)

def bfs(start):
    visited=[0 for _ in range(V+1)]
    visited[start]=1
    queue=deque()
    queue.append(start)
    cnt=1
    while len(queue)!=0:
        v=queue.popleft()
        for i in arr[v]:
            if visited[i]==0:
                visited[i]=1
                queue.append(i)
                cnt+=1
    return cnt

ans=[]
for i in range(1, V+1):
    ans.append(bfs(i))

m=max(ans)
for i in range(len(ans)):
    if ans[i]==m:
        print(i+1,end=' ')

'''import sys
sys.setrecursionlimit(100000)

V,E=map(int,input().split())
arr=[[] for _ in range(V+1)]
for _ in range(E):
    a,b=map(int,input().split())
    arr[b].append(a)

def dfs(start, n, visit, ans):
    visit[n]=1
    for i in arr[n]:
        if visit[i]==0:
            ans[start][0]+=1
            dfs(start, i, visit, ans)

ans=[[1,i] for i in range(V+1)]
for i in range(1, V+1):
    visit=[0 for _ in range(V+1)]
    dfs(i, i, visit, ans)

ans.sort()
for c,v in ans[1:]:
    if c==ans[-1][0]:
        print(v,end=' ')'''
