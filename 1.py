f_obj = open("new_f1.txt", 'a')
a = ' '
while a != '':
    a = input('введи строку!: ')
    f_obj.write(a)
    f_obj.write('\n')