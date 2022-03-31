class Stationery:
    def __init__(self,title):
        self.title = title
    def draw(self):
        print(f'запуск отрисовки')
class Pen(Stationery):
    def draw(self):
        print(f'рисование ручкой {self.title}')
class Pencil(Stationery):
    def draw(self):
        print(f'рисование карандашом {self.title}')
class Handle(Stationery):
    def draw(self):
        print(f'рисование маркером {self.title}')
Stationery_1 = Pen('Pilot')
Stationery_1.draw()
Stationery_2 = Pencil('М7')
Stationery_2.draw()
Stationery_1 = Handle ('красным')
Stationery_1.draw()