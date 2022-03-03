revenue = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))
if revenue > costs:
    print('выручка больше издержек')
    print((revenue-costs)/revenue)
    number_employee = int(input('Введите кол-во сотрудников: '))
    print((revenue-costs)/number_employee)
elif revenue == costs:
    print('выручка равна издержкам')
else:
    print(' издержки больше выручки')