import pandas as pd
import matplotlib.pyplot as plt
#перетвореня на датафрейм
try:
    df = pd.read_csv("comptagevelo2013.csv")
except FileNotFoundError:
    print("Файл не знайдено")
col = df.columns.drop("Date")
df[col] = df[col].astype("Int64")
#перевірка основних характеристик
print("Виведення 5 перших строк")
print(df.head())
print("\nВиведення стислої інформації про датафрейм")
print(df.info())
#Описова статистика
print("Описова статистика")
print(df.describe().round(0))
#загальну кількість велосипедистів за рік на усіх велодоріжках
DF = df.columns.drop("Date")
total = df[DF].sum()
print("Загальна кількість велосипедистів на усіх доріжках за 2013 рік: ", total.sum())
#загальну кількість велосипедистів за рік на кожній велодоріжці.
print("Загальна кількість велосипедистів за рік на кожній велодоріжці: ")
print(total)
#місяць найбільш популярний у велосипедистів, на кожній з  трьох з обраних велодоріжок.
roads = DF.to_list()
print("Список усіх велодоріжок:")
for i,name_road in enumerate(roads, 1):
    print(f"{i}. {name_road}")
#вибір 3 велодоріжок
print("Оберіть 3 велодоріжки")
choice = []
for i in range(3):
    a = (int(input(f"Введіть індекс {i+1} велодоріжки: ")))
    while a<1 or a>18:
        a = (int(input(f"Введено індекс, якого немає в списку\n"
                       f"Введіть правильний індекс {i + 1} велодоріжки: ")))
    choice.append(a-1)
selected = [roads[i] for i in choice]
sel_df = df[["Date"] + selected].copy()
sel_df["Date"] = pd.to_datetime(sel_df["Date"])
sel_df["Місяць"] = sel_df["Date"].dt.month_name()
Month = sel_df.groupby("Місяць")[selected].sum()
#Виведення результату - найпопулярніший місяць
final = Month.idxmax().reset_index()
final.columns = ["Доріжка", "Місяць"]
print("\nНайбільш популярний місяць у велосипедистів на 3 вибраних велодоріжках")
print(final)

#Побудова графіка
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
for i,name_road in enumerate(roads, 1):
    print(f"{i}. {name_road}")
choice = int(input("Оберіть велодоріжку, щоб побудувати для неї графік: "))
selected = roads[choice - 1]
sel_df = df[selected]
print("Дані обраної велодоріжки:")
print(sel_df)
sel_df.plot(label = "Кількість відвудувачів")
plt.title(f"Кількість відвідувачів велодоріжки {selected}")
plt.xlabel("Місяць")
plt.ylabel("Кількість відвідувачів")
plt.legend()
plt.show()