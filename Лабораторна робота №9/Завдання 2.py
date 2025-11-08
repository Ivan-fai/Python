import json
def Print(dict):#функція для виводу словника
    for i in dict:
        print("Марка:",i,", Вартість - ",dict[i][0],", Вік - ",dict[i][1])
def Add(dict,key,cost,age):#функція додавання елементу в словник
    if key in dict:
        dict[key][0] = cost
        dict[key][1] = age
        print("Оновлено значення марки ", key," : вартість:",dict[key][0], ", вік:", dict[key][1])
    else:
        dict[key] = [cost,age]
        print("Додано - Марка:", key,", Вартість:", dict[key][0],", Вік:",dict[key][1])
def Delete(dict,key):#видалення елементу із словника
    if key in dict:
        value = dict[key]
        del dict[key]
        print("Видалено - Марка:", key,", Вартість:", value[0],", Вік:",value[1])
    else:
        print("Марки не знайдено, виберіть іншу дію або введіть марку заново")
def Print_sorted(dict):#вивід відсортованого словника
    dict = {k:dict[k] for k in sorted(dict)}
    for i in dict:
        print("Марка:", i, ", Вартість - ", dict[i][0], ", Вік - ", dict[i][1])
def grater_than_six(dict):#визначення середньої вартості машин, рік яких більше 6
    Sum = 0
    i = 0
    for key in dict:
        if dict[key][1] > 6:
            Sum += dict[key][0]
            i = i + 1
    Average = Sum / i
    print('Середня вартість автомобілів, «вік» яких перевищує 6 років: результат записано до файлу Result.json')
    return Average
marks = {#словник
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
def Open_File(file_name,mode):#функція для безпечного відкриття файлу
    try:
        file = open(file_name,mode)
        return file
    except FileNotFoundError:
        print("Помилка відкриття файлу ",file_name)
def main():#функція для меню
    json_data = json.dumps(marks)
    file_json = Open_File("Dani.json","w")
    file_json.write(json_data)
    file_json.close()
    i = 1
    while i == 1:
        print("\nВведіть число для вибору функції:")
        choice = int(input("1 - Вивести словник на екран\n2 - Додати елемент до словника\n3 - Видалити елемент зі словника\n4 - Відсортувати словник\n5 - Знайти середню вартість марок, яким більше 6 років\n6 - Вийти\n"))
        if choice == 1:
            file_json = Open_File("Dani.json","r")#відкриття файлу
            json_text = file_json.read()#читання даних з файлу
            dict = json.loads(json_text)#десеріалізація даних
            Print(dict)
            file_json.close()
        elif choice == 2:
            file_json = Open_File("Dani.json","r")
            json_text = file_json.read()
            dict = json.loads(json_text)
            file_json.close()
            key = input("Введіть марку, яку хочете додати: ")
            while True:
                try:
                    cost = int(input(f"Введіть вартість для марки {key}:"))
                    age = int(input(f"Введіть вік для марки {key}:"))
                    Add(dict,key,cost,age)
                    break
                except ValueError:
                    print("Введено некоректне значення, введіть заново")
            json_data = json.dumps(dict)#серіалізація даних у джсон
            file_json = Open_File("Dani.json", "w")
            file_json.write(json_data)
            file_json.close()
            print("Дані були записані до файлу 'Dani.json'")
        elif choice == 3:
            file_json = Open_File("Dani.json","r")
            json_text = file_json.read()
            dict = json.loads(json_text)
            file_json.close()
            key = input("Введіть марку, яку хочете видалити: ")
            Delete(dict,key)
            json_data = json.dumps(dict)
            file_json = Open_File("Dani.json", "w")
            file_json.write(json_data)
            file_json.close()
        elif choice == 4:
            file_json = Open_File("Dani.json","r")
            json_text = file_json.read()
            dict = json.loads(json_text)
            Print_sorted(marks)
            file_json.close()
        elif choice == 5:
            file_json = Open_File("Dani.json", "r")
            json_text = file_json.read()
            dict = json.loads(json_text)
            average = grater_than_six(marks)
            file_json.close()
            file_json_res = Open_File("Result.json", "w")
            json_text = json.dumps(average)
            file_json_res.write(json_text)
            file_json_res.close()
        elif choice == 6:
            i = 0
        else:
            print("Введено некоректне значення введіть інше")
main()