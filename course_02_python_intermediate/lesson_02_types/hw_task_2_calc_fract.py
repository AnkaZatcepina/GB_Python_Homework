"""
    Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
    Программа должна возвращать сумму и произведение дробей. 
    Для проверки своего кода используйте модуль fractions.
"""
import re
from fractions import Fraction

# Нахождение общего делителя
def get_nod( a: int, b: int ) -> int:
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a   
    return(a + b)

# Сокращение дроби
def reduce_fract(a: int, b: int) -> str:   
    nod: int = get_nod(a, b)
    return '1' if a == b else f'{numerator//nod}/{denominator//nod}'

a_1, b_1, a_2, b_2 = map(int, re.split(" |/", input("Введите 2 дроби через пробел вида a/b: ")))

# Сложение
numerator = a_1*b_2 + a_2*b_1
denominator = b_1*b_2
print(f'Сумма дробей = {reduce_fract(numerator, denominator)}')

# Умножение
numerator: int = a_1*a_2
denominator: int = b_1*b_2
print(f'Произведение дробей = {reduce_fract(numerator, denominator)}')

# Проверка
print(f'Проверка суммы: {Fraction(a_1, b_1) + Fraction(a_2, b_2)}')
print(f'Проверка произведения: {Fraction(a_1, b_1) * Fraction(a_2, b_2)}')