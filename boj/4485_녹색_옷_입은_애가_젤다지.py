import heapq
import sys

N = int(input())
tc = 1
while N != 0:
    g = []
    for _ in range(N):
        g.append(list(map(int, input().split())))
    D = [[sys.maxsize for _ in range(N)] for _ in range(N)]

    q = []
    heapq.heappush(q, (0, 0, 0))
    D[0][0] = g[0][0]

    while q:
        dist, y, x = heapq.heappop(q)
        if D[y][x] < dist:
            continue
        if y < N-1:
            cost1 = D[y][x] + g[y+1][x]
            if cost1 < D[y + 1][x]:
                D[y + 1][x] = cost1
                heapq.heappush(q, (cost1, y + 1, x))
        if x < N-1:
            cost2 = D[y][x] + g[y][x+1]
            if cost2 < D[y][x+1]:
                D[y][x+1] = cost2
                heapq.heappush(q, (cost2, y, x+1))
        if y > 0:
            cost1 = D[y][x] + g[y-1][x]
            if cost1 < D[y-1][x]:
                D[y-1][x] = cost1
                heapq.heappush(q, (cost1, y-1, x))
        if x > 0:
            cost2 = D[y][x] + g[y][x-1]
            if cost2 < D[y][x-1]:
                D[y][x-1] = cost2
                heapq.heappush(q, (cost2, y, x-1))

    print("Problem " + str(tc) + ":", D[N-1][N-1])
    tc += 1
    N = int(input())