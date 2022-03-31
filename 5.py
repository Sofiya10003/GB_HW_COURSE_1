out_f = open("text_file.txt", "w")
str_list = '11 222 3333'
out_f.writelines(str_list)
print(f'Набор чисел, разделенных пробелами: {str_list}')
out_f.close()
out_f = open("text_file.txt", "r")
content = out_f.readline()
sum = 0
new_line = content.split()
for i in new_line:
    sum += int(i)
print(f'Сумма чисел в файле: {sum}')
out_f.close()