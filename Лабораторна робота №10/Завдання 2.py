import matplotlib.pyplot as plt
import numpy as np
import csv

try:
    file = open("Data.csv","r")
    reader = csv.DictReader(file, delimiter=';')
    years = []
    values_Ukraine = []
    values_UK = []
    for row in reader:
        years.append(int(row['Year']))
        values_Ukraine.append(float(row['Ukraine']))
        values_UK.append(float(row['United Kingdom']))
    file.close()
except FileNotFoundError:
    print("File exists")
x = np.array(years)
y_U = np.array(values_Ukraine)
y_UK = np.array(values_UK)
choice = int(input("Для побудови графіку з обома країнами натисніть 1, для стовпчатої діаграми натисність 2: "))
if choice == 1:
    plt.plot(x, y_U, label='Україна', color='green', linewidth=2, marker='o')
    plt.plot(x, y_UK, label='Велика Британія', color='purple', linewidth=2, marker='o')
    plt.title('Internet users (per 100 people)', fontsize=15)
    plt.xlabel('Рік', fontsize=15)
    plt.ylabel('Кількість користувачів', fontsize=15)
    y_range = np.arange(0, 100, 5)
    plt.xticks(x, rotation=45, ha='right', fontsize=10)
    plt.yticks(y_range, fontsize=10)
    plt.tight_layout()
    plt.grid(True)
    plt.legend()
    plt.show()
if choice == 2:
    choice = (input("Введіть країну для побудови графіку (Україна або Велика Британія): "))
    if choice == "Україна":
        plt.bar(years, y_U, label = 'Україна', color='green')
        plt.title('Internet users (per 100 people)', fontsize=15)
        plt.xlabel('Рік', fontsize=15)
        plt.ylabel('Кількість користувачів', fontsize=15)
        y_range = np.arange(0, 100, 5)
        plt.xticks(x, rotation=45, ha='right', fontsize=10)
        plt.yticks(y_range, fontsize=10)
        plt.tight_layout()
        plt.grid(False)
        plt.legend()
        plt.show()
        plt.show()
    if choice == "Велика Британія":
        plt.bar(years, y_UK, label = 'Велика Британія', color='purple')
        plt.title('Internet users (per 100 people)', fontsize=15)
        plt.xlabel('Рік', fontsize=15)
        plt.ylabel('Кількість користувачів', fontsize=15)
        y_range = np.arange(0, 100, 5)
        plt.xticks(x, rotation=45, ha='right', fontsize=10)
        plt.yticks(y_range, fontsize=10)
        plt.tight_layout()
        plt.grid(False)
        plt.legend()
        plt.show()
        plt.show()