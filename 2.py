class Division:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def error_devision(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f'Делитель {denominator } - поделить нельзя')

print(Division.error_devision(5, 0))
print(Division.error_devision(5, 2))