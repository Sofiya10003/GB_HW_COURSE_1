stroka = input('Введите несколько слов: ')
b = stroka.split(' ')
n = 0
for word in b:
    n += 1
    if len(word)<10 and len(word) != 0:
        print(f"{n}. {word}")
    elif len(word) == 0:
        print('Длина строки 0')
    else:
        print(f"{n}. {word[:10]}")