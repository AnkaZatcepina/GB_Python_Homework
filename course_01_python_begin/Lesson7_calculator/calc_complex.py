#Модуль для операций над комплексными числами


def multiply(complex_1,complex_2):
    return complex_1 * complex_2
def divide(complex_1,complex_2):
    return complex_1 / complex_2
def add(complex_1,complex_2):
    return complex_1 + complex_2
def subtract(complex_1,complex_2):
    return complex_1 - complex_2

def calc(str_1,str_2,operation):

    try:
        complex_1 = complex(str_1.replace(' ', ''))    
        complex_2 = complex(str_2.replace(' ', ''))
    except: 
        return 'Неверно введено число' 
    if operation == '*':
        return multiply(complex_1,complex_2)
    if operation == '/':   
        return divide(complex_1,complex_2)
    if operation == '+': 
        return add(complex_1,complex_2)
    if operation == '-': 
        return subtract(complex_1,complex_2)
    return 'Некорректно введена операция' 
         