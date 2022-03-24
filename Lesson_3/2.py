def f_parameters(name, surname, bith_date, city, email, mob_number):
    return f'{name}, {surname}, {bith_date}, {city}, {email}, {mob_number}'

print(f_parameters(name="Ivan", surname="Ivanov", bith_date='12.12.2012', city='Moscow', email='ivan@mail.ivan', mob_number='+7999999999'))