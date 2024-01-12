import heapq
N, K = map(int, input().split())
MAX = 100000
D = [MAX]*(MAX+1)

def dij(start, end):
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
                heapq.heappush(q, (dist+1, now*2))
            if now < MAX:
                heapq.heappush(q, (dist+1, now+1))
        if now > 0:
            heapq.heappush(q, (dist+1, now-1))

dij(N, K)
print(D[K])