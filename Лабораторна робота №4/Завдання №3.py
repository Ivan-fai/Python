def list_operations():
    print(f"Масив до вставки:\n{array}")
    k = int(input("Введіть кількість елементів, які хочете вставити: "))
    j = 0
    count_for_k = 0
    while count_for_k != k:
        if j % 2 != 0:
            new_element = int(input(f"Введіть елемент для вставки на позицію {j}: "))
            array.insert(j, new_element)#якщо індекс масиву непарний то вставляємо на його місце елемент
            count_for_k += 1
        j += 1
    print(f"Масив після вставки:\n{array}")

N = int(input("Введіть розмір масиву: "))
while N<0:
    N = int(input("Введено розмір масиву менше 0. Введіть коректний розмір масиву: "))
array =[int(input(f"Введіть елемент {i+1}: ")) for i in range(N)]
list_operations()