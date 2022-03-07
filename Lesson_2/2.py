number = list(input('Введите числа: '))
i=1
if len(number) % 2 == 0:
    while i != len(number) - 1:
        number[i], number[i-1] = number[i-1], number[i]
        i = i + 2
    number[len(number) - 1], number[len(number) - 2] =  number[len(number) - 2], number[len(number) - 1]
else:
    while i < len(number) - 1:
        number[i], number[i - 1] = number[i - 1], number[i]
        i = i + 2
print(number)