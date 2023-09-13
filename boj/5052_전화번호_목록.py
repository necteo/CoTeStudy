for _ in range(int(input())):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(input())
    trie = [[] for _ in range(10)]
    for p in arr:
        t = trie[int(p[0])]
        for i in p:
            if len(t) == 0:
                t = [[] for _ in range(10)]
                t = t[]
    print(trie)
