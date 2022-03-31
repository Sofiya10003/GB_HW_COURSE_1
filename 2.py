class Road:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def massa(self):
        return self.length * self.width * 25 * 5/1000

a = Road(20,5000)
print(f'Масса асфальта для дорожного полотна: {int(a.massa())} т')