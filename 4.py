class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print (f'автомобиль {self.name} поехал')
    def stop(self):
        print (f'автомобиль {self.name} остановилcя')
    def turn(self, direction):
        print (f'автомобиль {self.name} повернул {direction}')
    def show_speed(self):
        print (f'текущая скорость автомобиля {self.name}: {self.speed}')

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        print ('Cкорость превышена!' if self.speed > 60 else 'Cкорость не превышена')
class WorkCar(Car):
    def show_speed(self):
        print ('Cкорость превышена!' if self.speed > 40 else 'Cкорость не превышена')
class SportCar(Car):
    def go(self):
        print (f'Поехал спорткар - {self.color} {self.name} ')
class PoliceCar(Car):
    def go(self):
        print (f'Поехала полиция - {self.color} {self.name} виу виу')

car_1 = TownCar(50, 'красная', 'Девятка', False)
car_2 = WorkCar(80, 'черная', 'Калина', False)
car_3 = SportCar(100, 'синий', 'Шевролет', False)
car_4 = PoliceCar(80, 'белая', 'Шкода', True)
print(car_1.speed,car_1.color,car_1.name,car_1.is_police)
car_1.show_speed()
print(car_2.speed,car_2.color,car_2.name,car_2.is_police)
car_2.show_speed()
print(car_3.speed,car_3.color,car_3.name,car_3.is_police)
car_3.go()
print(car_4.speed,car_4.color,car_4.name,car_4.is_police)
car_4.go()
car_4.turn('направо')
car_4.stop()