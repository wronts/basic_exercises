# Вывести последнюю букву в слове
print('Задание 1:')
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
print('\nЗадание 2:')
word = 'Архангельск'
count = 0
for i in word.lower():
    if i == 'а':
        count += 1
print(count)


# Вывести количество гласных букв в слове
print('\nЗадание 3:')
word = 'Архангельск'
vowels =  ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
count = 0
for i in word.lower():
    if i in vowels:
        count += 1
print(count)


# Вывести количество слов в предложении
print('\nЗадание 4:')
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
print('\nЗадание 5:')
sentence = 'Мы приехали в гости'
for i in sentence.split():
    print(i[0])


# Вывести усреднённую длину слова в предложении
print('\nЗадание 6:')
sentence = 'Мы приехали в гости'
word_count = len(sentence.split())
words_lenght = len(sentence.replace(' ', ''))
print(words_lenght / word_count)