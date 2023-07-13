"""
    Пользователь вводит строку текста. Вывести каждое слово с новой строки.
    ✔ Строки нумеруются начиная с единицы.
    ✔ Слова выводятся отсортированными согласно кодировки Unicode.
    ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
    слова был один пробел между ним и номером строки.
"""


input_str = input(f'Введите строку: ')
words = sorted(input_str.split())
max_len = 0
for word in words:
    if len(word) > max_len:
        max_len = len(word)
for i, word in enumerate(words, start=1):
    print(f'{i}. {word:>{max_len}}')       