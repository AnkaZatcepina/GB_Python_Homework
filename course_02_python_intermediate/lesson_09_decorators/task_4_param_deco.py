"""
    📌 Создайте декоратор с параметром.
    📌 Параметр - целое число, количество запусков декорируемой
    функции.
"""

from typing import Callable

def param_deco(launch_qty: int) -> Callable:
    results = []
    def deco(func: Callable) -> Callable:
        def wrapper(*args,**kwargs):
            for _ in range(launch_qty):
                results.append(func(*args,**kwargs))
            return results
        return wrapper
    return deco

@param_deco(5)
def sum_nums(*args):
    return sum(args)

if __name__ == '__main__':
    print(sum_nums(1,2,3,4))