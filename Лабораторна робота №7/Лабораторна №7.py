def Open_file(file_name,mode):
    try:
        file = open(file_name,mode)

    except IOError:
        print("Не вдалося відкрити файл ", file_name)
        return None
    else:
        print("Вдалося відкрити файл ", file_name)
        return file
def main():
    simetric = []#список для зберігання симетричних слів
    file_1 = "TF15_1.txt"
    file_2 = "TF15_2.txt"
    file_1_w = Open_file(file_1,"w")
    if file_1_w!= None:
        string = input("Введіть текст: ")
        while string.isdigit():#якщо текст скалдається тільки з цифр
            string = input("Некоректний ввід.Введіть текст ще раз: ")
        file_1_w.write(string)#запис тексту у файл
        print("В файл TF15_1.txt додано текст: ", string)
        file_1_w.close()
    file_1_r  = Open_file(file_1,"r")
    file_2_w = Open_file(file_2,"w")
    if file_1_r!= None and  file_2_w!= None:#перевірка чи файли не пусті
        for block in file_1_r.read().split(","):#розбиття тексту на блоки при розділювачі кома
            for word in block.split(" "):# розбиття блоу на слова при розділювачі пробіл
                if word.lower() == word[::-1].lower():#умова:якщо поточне слово таке саме як і слово навпаки
                    simetric.append(word)
        file_2_w.write(" ".join(simetric))
        print("Симетричні слова записані у файл TF15_2.txt")
        file_1_r.close()
        file_2_w.close()
        print("Закрито файл TF15_1.txt та TF15_2.txt")
    file_2_r = Open_file(file_2,"r")
    print("Симетричні слова")
    if file_2_r!= None:
        for word in file_2_r.read().split():
            print(word)
main()