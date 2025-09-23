# Завдання №2
import math

for i in range(100, 0, -1):
    c = math.sqrt(i)
    if c == int(c):
        print("Корінь числа ",i, "= ",c)