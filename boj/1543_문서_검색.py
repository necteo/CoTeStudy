doc = input()
word = input()
i = 0
cnt = 0
while i < len(doc):
    k = i
    i += 1
    for j in range(len(word)):
        if k >= len(doc):
            break
        if doc[k] == word[j]:
            k += 1
        else:
            break
        if k-i+1 == len(word):
            i = k
            cnt += 1
print(cnt)