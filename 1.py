from time import sleep
class TrafficLight:
    def __init__(self):
        self.__color = ['красный', 'желтый', 'зеленый']
    def switching(self):
        while True:
            print(f'цвета светофора:{self.__color[0]}')
            sleep(7)
            print(f'цвета светофора:{self.__color[1]}')
            sleep(2)
            print(f'цвета светофора:{self.__color[2]}')
            sleep(3)
            print(f'цвета светофора:{self.__color[1]}')
            sleep(3)
a = TrafficLight()
a.switching()