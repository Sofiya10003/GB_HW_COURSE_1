def my_func(num_1, num_2, num_3):
    a = [num_1, num_2, num_3]
    b = min(a)
    if b == num_1:
        sum = num_2 + num_3
    if b == num_2:
        sum = num_1 + num_3
    if b == num_3:
        sum = num_1 + num_2
    return(sum)

print(my_func(5,4,6))