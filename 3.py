class NotNumber(ValueError):
    pass
my_list = []

while True:
    try:
        value = input('Введите числа через "enter":')

        if value == 'stop':
            print(f'Cписок введенных чисел: {my_list}')
            break

        if not value.isdigit():
            raise NotNumber(value)

        my_list.append(int(value))

    except NotNumber as ex:
        print('Было введено не число!', ex)
        print(f'Cписок введенных чисел: {my_list}')