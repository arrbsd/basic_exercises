# Вывести последнюю букву в слове
word = 'Архангельск'
last_letter = word[-1]
print("Последняя буква:", last_letter)

# Вывести количество букв "а" в слове
word = 'Архангельск'
count_letter_a = word.count('а')
print("Количество букв 'a':", count_letter_a)

# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = 'аеёиоуыэюя'
count_of_vowels = 0

for char in word:
    if char.lower() in vowels:
        count_of_vowels += 1
print("Количество гласных: ", count_of_vowels)



# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()
count_words = len(words)
print("Слов в предложении:", count_words)


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words = sentence.split()

for word in words:
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()

total_len = 0
for word in words:
    total_len = total_len + len(word)

print("Усредненная длин слова:", total_len / len(words))
