my_f = open(r"new_f_3.txt", "r")
content = my_f.readlines()
a = {}
people_number = 0
for line in content:
    people_number += 1
    b = line.split()
    a[b[0]]= b[1]
number_of_employees = people_number
print(a)
sum_salary = 0
for key,val in a.items():
    sum_salary += float(val)
    if float(val) < 20000:
        print(f'Фамиия сотрудника с з/п < 20 тысяч: {key}')
medium_fix_salary = sum_salary/number_of_employees
print(f'Средний оклад всех сотрудников: {medium_fix_salary}')
my_f.close()