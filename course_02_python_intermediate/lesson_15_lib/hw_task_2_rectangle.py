"""
Возьмите любые 1-3 задачи из прошлых домашних заданий.
Добавьте к ним логирование ошибок и полезной
информации. Также реализуйте возможность запуска из
командной строки с передачей параметров.
"""
import logging
import argparse

logging.basicConfig(filename='hw_task_2.log', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

def parse():
    parser = argparse.ArgumentParser(prog='create Rectangle', 
                                    description='Создание прямоугольника')
    parser.add_argument('-l', '--length', help='Длина прямоугольника')
    parser.add_argument('-w', '--width', help='Ширина прямоугольника')
    args = parser.parse_args()
    if args.length is None:
        rectangle = Rectangle(args.width)
    elif args.width is None:
        rectangle = Rectangle(args.length) 
    else:
        rectangle = Rectangle(args.length,args.width) 

    return rectangle

class NonPositiveNumberException(Exception):
    def __init__(self, value: int):
        self.value = value 
    def __str__(self):
        return f'Нельзя использовать число меньше или равное нулю "{self.value}"'

class Rectangle:
    def __init__(self, length: float, width: float | None = None):
        try:
            self.length = float(length)
        except ValueError as e:
            logger.error(f'Длину "{length}" не удалось привести к числу')
            raise
        try:
            self.width = float(width) if width != None else self.length
        except ValueError as e:
            logger.error(f'Ширину "{width}" не удалось привести к числу') 
            raise  
        if self.length <= 0:
            logger.error(NonPositiveNumberException(self.length))
            raise NonPositiveNumberException(self.length)  
        if self.width <= 0:
            logger.error(NonPositiveNumberException(self.width))            
            raise NonPositiveNumberException(self.length)
        logger.info(f'Создан {"прямоугольник" if width != None else "квадрат"} {self.length} x {self.width}')

  
    def get_perimeter(self)->int:
        return 2 * ( self.length + self.width )

    def get_area(self)->int:       
        return self.length * self.width  

if __name__ == '__main__':
    parse()
 