#coffee.py

coffee = 10
while True:
    money = int(input('돈내놔: '))
    if money == 300:
        print('확인')
        coffee = coffee - 1
    elif money > 300:
        print('꺼억')
        print(f'돈 드림: {money - 300}')
        coffee = coffee - 1
    else:
        print('뭐냐')
        print('남은 커피: {0}'.format(coffee))
    if coffee == 0:
        print('없다 가라')
        break
