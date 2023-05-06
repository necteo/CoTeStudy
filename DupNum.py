# DupNums.py

def DuplicateNumbers(number):           # 0~9사이의 문자로 된 숫자를 받는 함수
    for i in range(10):                 # 0~9사이의 i에서
        if number.count(str(i)) == 1:   # 입력받은 숫자에 0~9의 개수를 순서대로 확인 후 1개라면
            pass                        # 통과
        else:
            return False                # 아니라면 False
    return True                         # 전부 통과 즉 전부 1개씩이므로 True

numlist = input().split(' ')

for number in numlist:
    print(DuplicateNumbers(number), end = ' ')


def chkDupNum(s):
    result = []
    for n in s:
        if n in s:
            result.append(n)
        else:
            return False
    return len(result) == 10
