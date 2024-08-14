N, M = map(int, input().split())
city = []
home = []
chicken = []
for _ in range(N):
    city.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])

dis = [1000]*len(home)
for i in range(len(home)):
    for j in range(len(chicken)):
        d = max(i-x, x-i)+max(j-y, y-j)
        if dis[i] > d:
            dis[i] = d
