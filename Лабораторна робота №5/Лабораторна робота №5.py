def Print(marks):
    for i in marks:
        print("Марка:",i,", Вартість - ",marks[i][0],", Вік - ",marks[i][1])
def Add(marks,key,cost,age):
    if key in marks:
        marks[key][0] = cost
        marks[key][1] = age
        print("Оновлено значення марки ", key," : вартість:",marks[key][0], ", вік:", marks[key][1])
    else:
        marks[key] = [cost,age]
        print("Додано - Марка:", key,", Вартість:", marks[key][0],", Вік:",marks[key][1])
def Delete(marks,key):
    if key in marks:
        value = marks[key]
        del marks[key]
        print("Видалено - Марка:", key,", Вартість:", value[0],", Вік:",value[1])
    else:
        print("Марки не знайдено, виберіть іншу дію або введіть марку заново")
def Print_sorted(marks):
    print("Відсортований словник")
    marks = {k:marks[k] for k in sorted(marks)}
    for i in marks:
        print("Марка:", i, ", Вартість - ", marks[i][0], ", Вік - ", marks[i][1])
def grater_than_six(marks):
    Sum = 0
    i = 0
    for key in marks:
        if marks[key][1] > 6:
            Sum += marks[key][0]
            i = i + 1
    Average = Sum / i
    print("Середня вартість автомобілів, «вік» яких перевищує 6 років:",Average)
marks = {
    "Audi": [2000,1],
    "BMW":[2500,2],
    "Ford": [3000,3],
    "Lexus": [1750,4],
    "Chevrolet": [3400,5],
    "Kia": [2200,6],
    "Honda": [2800,7],
    "Nissan": [3500,8],
    "Toyota": [3200,9],
    "Skoda": [1900,10],
}
def main():
    i=1
    while i == 1:
        print("\nВведіть число для вибору функції:")
        choice = int(input("1 - Вивести словник на екран\n2 - Додати елемент до словника\n3 - Видалити елемент зі словника\n4 - Відсортувати словник\n5 - Знайти середню вартість марок, яким більше 6 років\n6 - Вийти\n"))
        if choice == 1:
            Print(marks)
        elif choice == 2:
            key = input("Введіть марку, яку хочете додати: ")
            while True:
                try:
                    cost = int(input(f"Введіть вартість для марки {key}:"))
                    age = int(input(f"Введіть вік для марки {key}:"))
                    Add(marks,key,cost,age)
                    break
                except ValueError:
                    print("Введено некоректне значення, введіть заново")
        elif choice == 3:
            key = input("Введіть марку, яку хочете видалити: ")
            Delete(marks,key)
        elif choice == 4:
            Print_sorted(marks)
        elif choice == 5:
            grater_than_six(marks)
        elif choice == 6:
            i = 0
        else:
            print("Введено некоректне значення введіть інше")
main()