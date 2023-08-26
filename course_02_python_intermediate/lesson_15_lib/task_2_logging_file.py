"""
    📌 На семинаре про декораторы был создан логирующий
    декоратор. Он сохранял аргументы функции и результат её
    работы в файл.
    📌 Напишите аналогичный декоратор, но внутри используйте
    модуль logging.
"""
from typing import Callable
import logging

logging.basicConfig(filename='task_2.log', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

def log_data(func: Callable):

    def wrapper(*args, **kwargs): 
        result = func(*args, **kwargs)
        data = {'args': args, **kwargs, 'result': result}
        logger.info(data)
        return result
    return wrapper 

@log_data
def division(a: int, b: int) -> float:
    try:
        result = a/b
    except ZeroDivisionError as e:
        logger.error(f'Деление на ноль! {e}')  
        result = float('inf')
    return result    

if __name__ == '__main__':    
    print(division(5, 3))    
    print(division(5, 2))    
    print(division(5, 0))