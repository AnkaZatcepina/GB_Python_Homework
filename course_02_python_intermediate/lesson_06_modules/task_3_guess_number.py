"""
    Улучшаем задачу 2. 
    Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала. 
    Строка должна принимать от 1 до 3 аргументов: параметры вызова функции. 
    Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.
"""

from random import randint
from sys import argv

def guess_numb(begin: int, end: int, attempts: int) -> bool:
    numb: int = 0
    rand_numb: int = randint(begin, end)
    for _ in range(attempts):
        numb = int(input(f'Введите число от {begin} до {end}: '))
        if numb == rand_numb:
            print('Верно!')
            return True
        elif numb < rand_numb:
            print('Больше') 
        elif numb > rand_numb:
            print('Меньше') 
    print('Количество попыток закончилось!')       
    return False

if __name__ == '__main__':
#    print(guess_numb(int(argv[1]),int(argv[2]),int(argv[3])))
    name, *param = argv
    print(guess_numb(*(int(elem) for elem in param)))