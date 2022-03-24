def int_func(my_word):
    up_word = my_word.title()
    return up_word

print(int_func('text'))

def int_func(my_word):
    up_word = my_word.title()
    return up_word

def func_2(my_line):
    list_line = []
    separated_line_list = my_line.split()
    for i in separated_line_list:
        list_line.append(int_func(i))
    str_line = " ".join(list_line)
    return str_line

print(func_2('check line first letter'))