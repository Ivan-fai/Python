import nltk
import matplotlib.pyplot as plt
from nltk import *
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import string
#Визначення кількості слів у тексті
parent = nltk.corpus.gutenberg.words("edgeworth-parents.txt")
print("Кількість слів у тексті:",len(parent))
#10 найбільш вживаних слів у тексті
fdist = FreqDist(parent)
top_ten = fdist.most_common(10)
print("10 найбільш вживаних слів")
print(top_ten)
x = [item[0] for item in top_ten]
y = [item[1] for item in top_ten]
#побудова графіку за 10 найбільш вживаними словами
plt.bar(x,y, color = "purple")
plt.title("Кількість найбільш вживаних слів у тексті")
plt.xlabel("Слова")
plt.ylabel("Кількість")
plt.show()
#Видалення знаків пунктуації
stop_words = set(stopwords.words("english"))
words = nltk.corpus.gutenberg.words("edgeworth-parents.txt")
without_stop_words = [word for word in words if not word in stop_words]
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in without_stop_words]
stripped = [w for w in stripped if w]
fdist = FreqDist(stripped)
top_ten = fdist.most_common(10)
print("10 найбільш вживаних слів після видалення знаків пунктуації")
print(top_ten)
#побудова графіку пілся видалення слів
x = [item[0] for item in top_ten]
y = [item[1] for item in top_ten]
plt.bar(x,y, color = "green")
plt.title("Кількість найбільш вживаних слів у тексті після видалення знаків пунктуації")
plt.xlabel("Слова")
plt.ylabel("Кількість")
plt.show()
