def f_two_number():
    try:
        first_n = int(input('Введите делимое'))
        second_n = int(input('Введите делитель'))
        division = first_n / second_n
        return division
    except ZeroDivisionError:
        print('делить на ноль нельзя')

print(f_two_number())