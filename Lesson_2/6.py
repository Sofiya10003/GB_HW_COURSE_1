quantity = int(input('Введите количество товаров: '))
my_list = []
names = []
prices = []
amount = []
units = []

number = 1
while number <= quantity:
    my_dict = {'Название': input('Введите название товара: '),
               'Цена': input('Введите цену: '),
               'Количество': input('Введите количество: '),
               'ед': input('Введите единицу измерения: ')
               }
    if my_dict['Название'] not in names:
        names.append(my_dict['Название'])
    if my_dict['Цена'] not in prices:
        prices.append(my_dict['Цена'])
    if my_dict['Количество'] not in amount:
        amount.append(my_dict['Количество'])
    if my_dict['ед'] not in units:
        units.append(my_dict['ед'])
    characteristic = (number, my_dict)
    my_list.append(characteristic)
    number += 1
for i in my_list:
    print(i)
analytics = {'Название:': names,
             'Цена:': prices,
             'Количество:': amount,
             'ед:': units}
for items in analytics.items():
    print(items)

quantity = int(input('Введите кол-во товаров: '))
my_list = []
name = []
price = []
quantity_goods = []
unit = []
number = 1
while number <= quantity:
    goods_dict = {'Название':input('введите название товара: '),
                    'Цена': input('введите стоимость товара: '),
                    'Количество': input('введите кол-во позиций товара: '),
                    'Единицы/штуки': input('введите ед измерения товара: ')}
    if goods_dict['Название'] not in name:
        name.append(goods_dict['Название'])
    if goods_dict['Цена'] not in price:
        price.append(goods_dict['Цена'])
    if goods_dict['Количество'] not in quantity_goods:
        quantity_goods.append(goods_dict['Количество'])
    if goods_dict['Единицы/штуки'] not in unit:
        unit.append(goods_dict['Единицы/штуки'])
    full_info = (number, goods_dict)
    my_list.append(full_info)
    number += 1
for i in my_list:
    print(i)
results = {'name': name,
        'price': price,
        'quantity_goods': quantity_goods,
        'unit': unit}
for items in results.items():
    print(items)