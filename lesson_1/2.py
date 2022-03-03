time = int(input('Введите время в секундах: '))
hour = time//3600
min = time % 3600 // 60
sek = time % 3600 % 60
if hour<10:
    hour='0'+ str(hour)
if min < 10:
    min = '0' + str(min)
if sek < 10:
    sek = '0' + str(sek)
print(f'{hour}:{min}:{sek}')