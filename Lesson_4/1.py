import sys
print(sys.argv)
from sys import argv
script_name, hours, rate, premium = argv
print("Итоговая зп: ", script_name)
print("Кол-во отработанных часов: ", hours)
print("Ставка в час: ", rate)
print("Премия: ", premium)

sum_salary = int(hours) * float(rate) + float(premium)
print(f'Зарплата сотрудника с учетом ставки: {sum_salary}')