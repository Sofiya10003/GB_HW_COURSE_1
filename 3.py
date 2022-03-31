class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
class Position(Worker):
    # def __init__(self, name, surname, position, income):
    #     super().__init__(name, surname, position, income)

    def get_full_name(self):
        return (f'Полное имя сотрудника:{self.name} {self.surname}')

    def get_total_income(self):
        return (f'Полный доход сотрудника {self.name} {self.surname}: {sum(self._income.values())}')

employee_1 = Position('ИВАН','ИВАНОВ','СЕНЬОР',10000,4000)

print(employee_1.get_full_name())
print(employee_1.get_total_income())