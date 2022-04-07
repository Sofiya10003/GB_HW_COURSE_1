class Kletka:
    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f"результат: {self.quantity}"

    def __add__(self, other):
        return Kletka(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity >= other.quantity:
            return Kletka(self.quantity - other.quantity)
        else:
            return f"кол-во клеток в первом случае меньше"

    def __mul__(self, other):
        return Kletka(self.quantity * other.quantity)

    def __truediv__(self, other):
        return Kletka(round(self.quantity / other.quantity))

    def make_order(self, number_in_row):
        self.number_in_row = number_in_row
        row = int(self.quantity / self.number_in_row)
        new_str = ''
        for i in range(row):
            new_str += '*'* number_in_row + '\n'
        new_str += '*'* (self.quantity % self.number_in_row)
        return new_str


kl_1 = Kletka(14)
kl_2 = Kletka(10)
print(kl_1 + kl_2)
print(kl_1 - kl_2)
print(kl_1 * kl_2)
print(kl_1 / kl_2)

print(kl_1.make_order(3))