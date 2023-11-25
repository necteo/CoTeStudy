import heapq

MAX = 100000
N, K = map(int, input().split())
t = 0
D = [MAX]*(MAX+1)

def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, start))
    D[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if D[now] < dist:
            continue
        D[now] = dist
        if now == end:
            break
        if now < end:
            if now != 0 and now*2 <= MAX:
                heapq.heappush(q, (dist, now*2))
            if now < MAX:
                heapq.heappush(q, (dist+1, now+1))
        if now > 0:
            heapq.heappush(q, (dist+1, now-1))

dijkstra(N, K)
print(D[K])