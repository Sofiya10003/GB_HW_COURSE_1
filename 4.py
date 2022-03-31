my_f = open(r"new_f.txt", "r+", encoding='utf-8')
content = my_f.readlines()
for line in content:
    s = line.split()
    for i in range(0,len(s)):
        if s[0] =='One':
            s[0] = 'Один'
        elif s[0] =='Two':
            s[0] = 'Два'
        elif s[0] =='Three':
            s[0] = 'Три'
        elif s[0] =='Four':
            s[0] = 'Четыре'
    print(s)
    new_line_s = f'{s[0]} {s[1]} {s[2]}'
    my_f_2 = open(r"new_f_4.txt", "a", encoding='utf-8')
    content_2 = my_f_2.writelines(new_line_s)
    my_f_2.write('\n')
my_f.close()
my_f_2.close()