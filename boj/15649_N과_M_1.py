n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)]
check = [False for _ in range(len(arr))]
tmp = []
ans = []


def perm(idx, N, R):
    if idx == R:    # 원하는 개수 R 만큼 고르면
        for v in tmp:
            print(v, end=" ")
        print()
        return
    for i in range(N):  # N개 만큼
        if not check[i]:    # i를 앞에서 고르지 않았다면
            check[i] = True # i를 고름
            tmp.append(arr[i])  # 현재 고르는 중인 배열 tmp에 idx번째 수를 추가
            perm(idx + 1, N, R) # 다음 번째 수를 고른다
            tmp.pop()   # 이미 ans에 저장했기 때문에 빼내고 tmp의 길이는 1감소
            check[i] = False    # tmp에서 빼냈기 때문에 고르지 않았다는 의미가 된다


perm(0, n, m)
