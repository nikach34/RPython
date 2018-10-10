import math

iterations = 20

def my_exp(x):
    """Вычисление синуса при помощи частичного суммирования ряда Тейлора"""
    x_pow = x
    multiplier = 1
    partial_sum = x
    for n in range(1, iterations):
        x_pow *= x  
        multiplier *= 1 / (n) 
        partial_sum += x_pow * multiplier
    
    return partial_sum

print(help(math.sin), math.sin(0.4))
print(help(my_exp), my_exp(15))
