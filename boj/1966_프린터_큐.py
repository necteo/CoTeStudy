for _ in range(int(input())):
    N, M = map(int, input().split())
    q = list(map(int, input().split()))
    cnt = [0 for _ in range(10)]
    for i in q:
        cnt[i] += 1
    last = N-1
    idx = 0
    ans = 0
    for i in range(9, 0, -1):
        while cnt[i]:
            if q[idx] == i:
                cnt[i] -= 1
                ans += 1
                if idx == M:
                    print(ans)
            else:
                q.append(q[idx])
                last += 1
                if idx == M:
                    M = last
            idx += 1