number = int(input('Введите число от 1 до 12: '))
seasons_dict = {"winter": (12,1,2), "spring": (3,4,5),"summer": (6,7,8), "autumn": (9,10,11) }
if number in range(1,13):
    for key in seasons_dict.keys():
        if number in seasons_dict[key]:
            print(key)