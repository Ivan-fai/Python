import csv
import os
try:
    file_csv = open("Dani.csv","r")
    reader = csv.DictReader(file_csv, delimiter = ";")#читання файлу та перетворення у словник
    print("Country Code: UKR")
    for row in reader:
        print(row['Country Code'], ': ', row['UKR'])#вивід на екран даних
    file_csv.close()
except FileNotFoundError:
    print("Файл Dani.csv не знайдено!")
try:
    file_csv = open("Dani.csv","r")
    file_csv_write = open("Result.csv","w", newline="")
    reader = csv.DictReader(file_csv, delimiter = ";")
    dictionary = dict(#ствоерння словника для пошуку мін та макс значення
        (row['Country Code'], row['UKR'])
        for row in reader
    )
    min_value = min(dictionary.values())#пошук мінімального значення
    max_value = max(dictionary.values())#пошук максимального значення
    writer = csv.writer(file_csv_write, delimiter=";")
    #запис знайдених чисел у новий файл
    writer.writerow(["Найменше значення:",min_value])
    writer.writerow(["Найбільше значення:",max_value])
    print("Найменше та найбільше значення було записано у файл Result.csv")
    file_csv.close()
    file_csv_write.close()
except FileNotFoundError:
    print("Не вдалося відкрити файл Dani.csv")