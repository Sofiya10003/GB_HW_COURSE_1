my_dict={}
my_f = open(r"text_file_7.txt", "r", encoding='utf-8')
content = my_f.readlines()
avg_profit = 0
for line in content:
    list_line = line.split()
    for i in range(0,len(list_line)):
        key_n = list_line[0]
        profit_loss = abs(int(list_line[2]) - int(list_line[3]))
        my_dict[key_n] = profit_loss
        if (int(list_line[2]) - int(list_line[3])) > 0:
            avg_profit += int(list_line[2]) - int(list_line[3])
    avg_total = avg_profit/len(content)
    print(avg_total)
    print(my_dict)

my_f.close()