s = str(input("Введіть речення: "))
words = s.split()
sorted_words = sorted(words, key = len)#сортування за довжиною за зростанням
print("\n".join(sorted_words))