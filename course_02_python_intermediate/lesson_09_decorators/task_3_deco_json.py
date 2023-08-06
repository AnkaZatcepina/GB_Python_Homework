"""
    📌 Напишите декоратор, который сохраняет в json файл
    параметры декорируемой функции и результат, который она
    возвращает. При повторном вызове файл должен
    расширяться, а не перезаписываться.
    📌 Каждый ключевой параметр сохраните как отдельный ключ
    json словаря.
    📌 Для декорирования напишите функцию, которая может
    принимать как позиционные, так и ключевые аргументы.
    📌 Имя файла должно совпадать с именем декорируемой
    функции.
"""
import json
import os
from typing import Callable

def add_params_to_json( func:Callable )-> Callable[[], None ]:
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

@add_params_to_json
def sum_nums(*args, **kwargs)->int:
    return sum(args) 

@add_params_to_json
def concat_str(*args, **kwargs)->str:
    return ''.join(args)     

if __name__ == '__main__':
    sum_nums(1,2,3, x=5,y=6,z=7)    
    concat_str('aa','b','cccc', word='test')             