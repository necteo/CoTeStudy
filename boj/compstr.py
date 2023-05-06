# compstr.py

list = 'aaabbcccccca'
result = []
count = 1

for i in range(len(list)):
    if i + 1 < len(list):
        if list[i] == list[i + 1]:
            count += 1
        else:
            result.append(list[i] + str(count))
            count = 1
    else:
        result.append(list[i] + str(count))

print(('').join(result))

result = ""
_c = ''
cnt = 0

for c in list:
    if c != _c:
        _c = c
        if cnt: result += str(cnt)
        result += c
        cnt = 1
    else:
        cnt += 1
if cnt: result += str(cnt)
print(result) 
