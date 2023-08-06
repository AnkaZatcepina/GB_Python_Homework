"""
Напишите следующие функции:
    ○ Нахождение корней квадратного уравнения
    ○ Генерация csv файла с тремя случайными числами в каждой строке.
    100-1000 строк.
    ○ Декоратор, запускающий функцию нахождения корней квадратного
    уравнения с каждой тройкой чисел из csv файла.
    ○ Декоратор, сохраняющий переданные параметры и результаты работы
    функции в json файл.
"""
import csv
import json
from random import randint
from random import choice
from typing import Callable

def save_to_json(file_path: str)-> Callable:
    def save(func: Callable)-> Callable:
        def wrapper(*args,**kwargs):
            data = []
            curr_data = {
                'args': args,
                **kwargs
            }               
            result = func(*args,**kwargs)
            curr_data['result'] = str(result)
            data.append(curr_data)
            with open(file_path, 'a', encoding='utf-8') as json_file:
                json.dump(data, json_file, indent=2, ensure_ascii = False) 
            return result                          
        return wrapper
    return save    


def solve_from_csv(file_path: str) -> Callable:
    results = []
    def solve(func: Callable)-> Callable:
        def wrapper(*args,**kwargs):
            data = []
            with open(file_path, 'r', encoding='utf-8') as csv_file:
                for row in csv.reader(csv_file, dialect='excel'):
                    a,b,c = map(int,row)
                    results.append(func(a,b,c))  
            return results                           
        return wrapper
    return solve
            

def generate_csv_quadratic_coeff(file_path: str = 'hw_task_1.csv')->None:
    MIN_VAL = -100
    MAX_VAL = 100
    ROWS_AMOUNT = 100
    with open(file_path, 'w', encoding='utf-8') as csv_file: 
        csv_writer = csv.writer(csv_file, dialect='excel',quoting=csv.QUOTE_MINIMAL) 
        for _ in range(ROWS_AMOUNT):      
            csv_writer.writerow([
            choice([i for i in range(MIN_VAL, MAX_VAL+1) if i != 0]), 
            randint(MIN_VAL, MAX_VAL+1), 
            randint(MIN_VAL, MAX_VAL+1)
            ])
            


@solve_from_csv('hw_task_1.csv')
@save_to_json('hw_task_1.json')
def solve_quadratic_equation(a: float, b: float, c: float) -> float | tuple[float,float] | tuple[complex,complex]:
    d = b**2 - 4*a*c
    if d > 0:
        x_1 = (-b - d**0.5)/(2*a)
        x_2 = (-b + d**0.5)/(2*a)
        return(x_1,x_2)
    elif d == 0:
        x = -b/(2*a)  
        return(x)
    else:
        d = complex(d,0)
        x_1 = (-b - d**0.5)/(2*a)
        x_2 = (-b + d**0.5)/(2*a)           
        return(x_1,x_2)

if __name__ == '__main__':
    generate_csv_quadratic_coeff()
    for res in solve_quadratic_equation():
        print(str(res))  
