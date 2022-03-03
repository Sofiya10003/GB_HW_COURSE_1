number = int(input('Введите число: '))
b = 0
while number > 0:
    a = number%10
    if a > b:
        b = a
    number = number//10
    print(a, b, number)
print(b)