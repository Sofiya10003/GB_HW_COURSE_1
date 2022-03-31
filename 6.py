my_dict = {}
my_f = open(r"python.txt", "r+", encoding='utf-8')
content = my_f.readlines()
for line in content:
    list_line = line.split()
    total_amount = 0
    for i in range(0,len(list_line)):
        if i > 0 and list_line[i] !='—':
            one_piece = list_line[i].split('(')
            total_amount += int(one_piece[0])
            my_dict[list_line[0][:-1]] = total_amount
print(my_dict)
my_f.close()