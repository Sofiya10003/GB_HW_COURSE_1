class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return f'Дата в числовом формате: {int(my_date[0])}, {int(my_date[1])}, {int(my_date[2])}'


    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    return f'{day}, {month}, {year} - дата корректная'
                else:
                    return f'{day}, {month}, {year} - год указан некорректно'
            else:
                return f'{day}, {month}, {year} - месяц указан некорректно'
        else:
            return f'{day}, {month}, {year} - день указан некорректно'


print(Data.extract('02 - 02 - 2022'))

print(Data.valid(1, 12, 2012))
print(Data.valid(12, 11, 2025))
print(Data.valid(12, 13, 2025))
print(Data.valid(35, 11, 2025))