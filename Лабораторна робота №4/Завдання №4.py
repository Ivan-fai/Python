def switch ():
    N = int(input("Введіть розмір масиву: "))
    while N < 0:
        N = int(input("Введено розмір масиву менше 0. Введіть коректний розмір масиву: "))
    array = [int(input(f"Введіть елемент {i + 1}: ")) for i in range(N)]
    print("Масив до змін")
    print(" ".join(map(str, array)))
    Max = max(array)#отримання макс. числа масиву
    Min = min(array)#отримання мін. числа масиву
    #отримання індексів макс. і мін. числа
    min_index = array.index(Min)
    max_index = array.index(Max)
    array[max_index], array[min_index] = array[min_index], array[max_index]#міняємо їх місцями
    print("Масив після змін")
    print(" ".join(map(str, array)))

switch ()