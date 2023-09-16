from collections import deque

while True:
    w,h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = []
    for _ in range(h):
        arr.append(list(map(int, input().split())))
    cnt = 0
    visit = [[0 for _ in range(w)] for _ in range(h)]
    for y in range(h):
        for x in range(w):
            queue = deque()
            queue.append([x, y])
            chk = 0
            while queue:
                v,u = queue.popleft()
                if arr[u][v] == 1:
                    if visit[u][v] == 0:
                        visit[u][v] = 1
                        chk = 1
                        if v > 0:
                            queue.append([v-1,u])
                            if u > 0:
                                queue.append([v-1, u-1])
                            if u < h-1:
                                queue.append([v-1, u+1])
                        if v < w-1:
                            queue.append([v+1,u])
                            if u > 0:
                                queue.append([v+1, u-1])
                            if u < h-1:
                                queue.append([v+1, u+1])
                        if u > 0 :
                            queue.append([v,u-1])
                        if u < h-1:
                            queue.append([v,u+1])
            if chk == 1:
                cnt += 1
    print(cnt)