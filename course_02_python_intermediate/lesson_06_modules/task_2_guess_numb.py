"""
    Создайте модуль с функцией внутри. 
    Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток. 
    Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток. 
    Функция выводит подсказки “больше” и “меньше”. 
    Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
"""
from random import randint

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
    print(guess_numb(1,10,4))