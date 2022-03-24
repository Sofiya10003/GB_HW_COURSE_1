def func_line():
    line = 0
    number_in_line = 0
    sum_numbers = 0
    special_letter = 'q'
    while True:
        line = input('Введите строку чисел, разделенных пробелом: ')
        b = line.split()
        l = []
        for i in range(0,len(b)):
            if b[i] == special_letter:
                break
            else:
                number_in_line = int(b[i])
            sum_numbers = sum_numbers + number_in_line
        print(f'Cумма чисел в строках(е) равна: {sum_numbers}')
func_line()