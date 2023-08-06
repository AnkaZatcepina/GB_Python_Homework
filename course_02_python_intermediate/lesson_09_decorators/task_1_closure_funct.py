"""
    📌 Создайте функцию-замыкание, которая запрашивает два целых
    числа:
        ○ от 1 до 100 для загадывания,
        ○ от 1 до 10 для количества попыток
    📌 Функция возвращает функцию, которая через консоль просит
    угадать загаданное число за указанное число попыток.
"""
from typing import Callable


def guess_numb(numb:int, attempts:int) -> Callable[[], None]:
    def guess_numb_closure():
        for i in range(1, attempts+1):
            print(f'Номер попытки {i}')
            answer = int(input(f'Введите число от 1 до 100:'))
            if answer == numb:
                print('Верно!')
                breakс
    return guess_numb_closure


if __name__ == '__main__':
   game = guess_numb(15,4)
   game() 


