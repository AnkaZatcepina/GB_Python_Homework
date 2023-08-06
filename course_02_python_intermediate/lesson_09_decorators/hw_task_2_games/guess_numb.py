"""
    Угадайка чисел:
        ○ от 1 до 100 для загадывания,
        ○ от 1 до 10 для количества попыток
"""

__all__ = ['guess_numb', 'deco']

import random
from typing import Callable


def deco(func: Callable) -> Callable[[int,int], None]:
    MIN_NUMB = 1
    MAX_NUMB = 100
    MIN_ATTEMPTS = 1
    MAX_ATTEMPTS = 10

    def wrapper(numb:int, attempts:int, *args, **kwargs):
        if not MIN_NUMB <= numb <= MAX_NUMB:
            numb = random.randint(MIN_NUMB, MAX_NUMB+1)
        if not MIN_ATTEMPTS <= attempts <= MAX_ATTEMPTS:
            attempts = random.randint(MIN_ATTEMPTS, MAX_ATTEMPTS+1)    
        return func(numb, attempts, *args, **kwargs)
    return wrapper    

@deco    
def guess_numb(numb:int, attempts:int):
    for i in range(1, attempts+1):
        print(f'Номер попытки {i}')
        answer = int(input(f'Введите число от 1 до 100:'))
        if answer == numb:
            print('Верно!')
            break
        elif answer > numb:
            print('Меньше')
        else:
            print('Больше')




if __name__ == '__main__':
   guess_numb(700,55)