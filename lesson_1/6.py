a = float(input('Введите a - км в 1-ый день: '))
b = float(input('Введите b - требуемое кол-во км: '))
number_days = 1
while a < b:
    a = a+a*0.1
    number_days = number_days+1
print(number_days)