# 1line_ggd.py

def ggd(n):
    for i in range(1, 10):
        print(n * i, end = ' ')

n = int(input("구구단을 출력할 숫자를 입력하세요(2~9): "))
ggd(n)
