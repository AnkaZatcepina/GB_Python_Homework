"""
    ✔ Напишите функцию, которая заполняет файл
    (добавляет в конец) случайными парами чисел.
    ✔ Первое число int, второе - float разделены вертикальной чертой.
    ✔ Минимальное число - -1000, максимальное - +1000.
    ✔ Количество строк и имя файла передаются как аргументы функции.
"""
__all__ = ['append_file_random', ]

import random

MIN_INT: int = -1000
MAX_INT: int = 1000

def append_file_random(filename: str = 'task_1_file.txt', limit: int = 10):
    with open(filename, mode='a', encoding='utf-8') as file:
        for _ in range(limit):
            first: int = random.randint(MIN_INT, MAX_INT)
            second: float = random.uniform(MIN_INT, MAX_INT)
            file.write(str(first) + '|' + str(second) + '\n')


if __name__ == '__main__':
    append_file_random()