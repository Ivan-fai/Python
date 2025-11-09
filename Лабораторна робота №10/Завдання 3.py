import matplotlib.pyplot as plt
import numpy as np
import csv
def New_format(pct):
    absolute = (pct / 100.) * total
    return '{:.1f}%\n({:.1f})'.format(pct, absolute)# Повертаємо відформатований рядок
try:
    file = open("Dani1.csv","r")
    reader = csv.DictReader(file, delimiter=';')
    years = []
    values = []
    for row in reader:
        years.append(int(row['Country Code']))
        values.append(float(row['UKR']))
    file.close()
except FileNotFoundError:
    print("File exists")
x = np.array(years)
y = np.array(values)
total = sum(y)
labels = x.tolist()
fig, ax = plt.subplots(figsize=(8, 7))
ax.pie(y,labels=labels,autopct=New_format,startangle=90,textprops={'fontsize': 10})
plt.title('GDP Life expectancy at birth, total (years)',fontsize = 10)
plt.axis('equal')
plt.show()