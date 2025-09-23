import math
def calculate_z(x):
    z=float(1-2*(math.sin(x))**2)/(1+(math.sin(x))**2)
    return z

def sum_of_even_num(x, y):
    sum_even = 0
    for i in range(x, y + 1):
        if i % 2 == 0:
            sum_even += i
    return sum_even

x = float(input("Введіть значення х: "))
z = calculate_z(x)
print("Значення z = ", z)

