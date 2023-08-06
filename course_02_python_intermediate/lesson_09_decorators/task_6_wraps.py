"""
    📌 Доработайте прошлую задачу добавив декоратор wraps в
    каждый из декораторов.
"""
import random
import json
import os
from typing import Callable
from functools import wraps


def validate(func: Callable) -> Callable[[int,int], None]:
    MIN_NUMB = 1
    MAX_NUMB = 100
    MIN_ATTEMPTS = 1
    MAX_ATTEMPTS = 10

    @wraps(func)
    def wrapper(numb:int, attempts:int, *args, **kwargs):
        if not MIN_NUMB <= numb <= MAX_NUMB:
            numb = random.randint(MIN_NUMB, MAX_NUMB+1)
        if not MIN_ATTEMPTS <= attempts <= MAX_ATTEMPTS:
            attempts = random.randint(MIN_ATTEMPTS, MAX_ATTEMPTS+1)    
        return func(numb, attempts, *args, **kwargs)
    return wrapper    

def add_params_to_json( func:Callable )-> Callable[[], None ]:
    @wraps(func)
    def wrapper(*args,**kwargs):
        file_path = f'{func.__name__}.json'
        data = []
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)  
        curr_data = {
            'args': args,
            **kwargs
        }    
        result = func(*args,**kwargs)
        curr_data['result'] = result
        data.append(curr_data)
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=2, ensure_ascii = False)
        return result    
    return wrapper 

def launch_qty(launch_qty: int) -> Callable:
    results = []
    def deco(func: Callable) -> Callable:
        
        @wraps(func)
        def wrapper(*args,**kwargs):
            for _ in range(launch_qty):
                results.append(func(*args,**kwargs))
            return results
        return wrapper
    return deco

@launch_qty(3)
@validate
@add_params_to_json
def guess_numb(numb:int, attempts:int):
    """My documentation"""
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
    guess_numb(15, 2)
    print(f'{guess_numb.__name__ = }')
    print(f'{guess_numb.__doc__ = }')