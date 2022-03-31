from itertools import cycle
list = [12,24,37,4,5,6]
с = 0
for el in cycle(list):
    if с > 10:
        break
    print(el)
    с += 1