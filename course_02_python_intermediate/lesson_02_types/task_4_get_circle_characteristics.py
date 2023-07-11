"""
    ✔ Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
    ✔ Диаметр не превышает 1000 у.е.
    ✔ Точность вычислений должна составлять не менее 42 знаков после запятой.
"""
import math
import decimal

MAX_DIAMETR: int = 1000
decimal.getcontext().prec = 42
PI: decimal.Decimal = decimal.Decimal(math.pi)

diametr: decimal.Decimal = decimal.Decimal(input('Введите диаметр:'))
if diametr <= 0 or diametr > MAX_DIAMETR:
    print('Некорректно введён диаметр')
    exit()
print(f'Площадь круга = {PI*(diametr/2)**2}')
print(f'Длина окружности = {PI*diametr}')