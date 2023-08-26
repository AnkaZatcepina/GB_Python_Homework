"""
📌 Доработаем задачу 2.
📌 Сохраняйте в лог файл раздельно:
    ○ уровень логирования,
    ○ дату события,
    ○ имя функции (не декоратора),
    ○ аргументы вызова,
    ○ результат.
"""

from typing import Callable
import logging

FORMAT = '{levelname} - {asctime} - {msg}'
logging.basicConfig(filename='task_3.log', encoding='utf-8', level=logging.INFO, format=FORMAT, style='{')
logger = logging.getLogger(__name__)

def log_data(func: Callable):

    def wrapper(*args, **kwargs): 
        result = func(*args, **kwargs)
        data = {'args': args, **kwargs}
        msg = f'{func.__name__}: {data}. Result: {result}'
        logger.info(msg)
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