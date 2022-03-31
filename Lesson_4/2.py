old_list = [1, 2, 1, 4, 3, 6, 5, 8, 7, 9]
new_list = [number for i,number in enumerate(old_list) if old_list[i] > old_list[i-1]]
print(f"Исходный список: {old_list}")
print(f"Новый список: {new_list}")