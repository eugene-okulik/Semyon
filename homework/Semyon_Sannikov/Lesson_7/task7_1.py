parametr = 13

while True:
    user_input = int(input('Введи цифру, пользователь: '))
    if user_input == parametr:
        print('Поздравляю! Вы угадали!')
        break
    else:
        print('попробуйте снова')
