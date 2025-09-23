n = int(input("Введіть n від 1 до 9 "))
while n < 1 or n > 9:
    n = int(input("Введіть коректне значення n від 1 до 9 "))
X = n
for i in range(1, n + 1):
    num = n
    for j in range(n, 0, -1):
        if j > X:
            print(" ", end=" ")
            num -= 1
        else:
            print(num, end=" ")
            num -= 1
    X -= 1
    print("")