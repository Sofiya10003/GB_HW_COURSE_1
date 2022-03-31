my_f = open(r"new_f_2.txt", "r")
content = my_f.readlines()
a = {}
number = 1
for i in content:
    a[number] = len(i.split())
    number += 1
print(f'содержание файла:{content}')
print(f'кол-во введенных строк:{len(content)}')
print(f'строка/кол-во слов в строке:{a}')
my_f.close()