#Модуль для операций над рациональными числами
from fractions import Fraction

def multiply(rational_1,rational_2):
    return rational_1 * rational_2
def divide(rational_1,rational_2):
    return rational_1 / rational_2
def add(rational_1,rational_2):
    return rational_1 + rational_2
def subtract(rational_1,rational_2):
    return rational_1 - rational_2

def calc(str_1,str_2,operation):
    try:
        rational_1 = Fraction(str_1.replace(' ', ''))    
        rational_2 = Fraction(str_2.replace(' ', ''))
    except:         
        return 'Неверно введено число'
    if operation == '*':
        return multiply(rational_1,rational_2)
    if operation == '/':   
        return divide(rational_1,rational_2)
    if operation == '+': 
        return add(rational_1,rational_2)
    if operation == '-': 
        return subtract(rational_1,rational_2)
    return 'Некорректно введена операция' 