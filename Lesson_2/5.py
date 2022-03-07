my_list = [7, 5, 3, 3, 2]
user_digit = int(input('Введите число: '))
quantity_element = len(my_list)
for i in range(0,len(my_list)-1):
    if my_list[i] <= user_digit:
        my_list.insert(i, user_digit)
        break
if len(my_list)== quantity_element:
    my_list.append(user_digit)
print(my_list)