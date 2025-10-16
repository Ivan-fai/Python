N = int(input("Введіть розмір масиву: "))
while N<0:
    N = int(input("Введено розмір масиву менше 0. Введіть коректний розмір масиву: "))
array = [int(input()) for _ in range(N)]#заповнення масиву користувачем
negative = []#створення масиву для від'ємних елементів
for element in array:
    if element<0:
        negative.append(element)
negative.reverse()#обератння масиву для виведення у зворотньому нарямку
print(" ".join(map(str, negative)))