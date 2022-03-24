def my_func(x,y):
    b = x
    i = 1
    while i < abs(y):
        i = i+1
        b = b * x
    return (1/b)

print(my_func(2,-2))