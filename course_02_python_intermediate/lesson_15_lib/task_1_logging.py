"""
    Напишите программу, которая использует модуль logging для
    вывода сообщения об ошибке в файл.
    Например отлавливаем ошибку деления на ноль.
"""
import logging

logging.basicConfig(filename='task_1.log', level=logging.ERROR, encoding='utf-8')

def division(a: int, b: int) -> float:
    try:
        result = a/b
    except ZeroDivisionError as e:
        logging.error(f'Деление на ноль! {e}')  
        result = float('inf')
    return result    

if __name__ == '__main__':
    print(division(5, 0))
