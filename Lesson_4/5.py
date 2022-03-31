list = ([el for el in range(100,1001) if el % 2 == 0])
from functools import reduce
def my_func(prev_element, element):
    return prev_element * element
result = reduce(my_func, list)
print(f'Результат умножения четных чисел из диапозона от 100 до 1000: {result}')