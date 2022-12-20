#Калькулятор для работы с рациональными и комплексными числами
import calc_complex
import calc_rational
import logger

def get_operation():
    operation = input('Введите операцию: * / + -: ')
    return operation

print('Это калькулятор, который складывает рациональные и комплексные числа')
print('Введите тип чисел:')
print('1 - рациональные')
print('2 - комплексные')
number_type = int(input(''))
if number_type == 1:
    rational_1 = input('Введите первое рациональное число в формате [a]/[b]: ')
    rational_2 = input('Введите второе рациональное число в формате [a]/[b]: ')
    operation = get_operation()
    result = calc_rational.calc(rational_1,rational_2,operation)
    logger.log(rational_1, rational_2, operation, result)
elif number_type == 2:
    complex_1 = input('Введите первое комплексное число в формате [a]+[b]j: ')
    complex_2 = input('Введите второе комплексное число в формате [a]+[b]j: ')
    operation = get_operation()
    result = calc_complex.calc(complex_1,complex_2,operation)
    logger.log(complex_1, complex_2, operation, result)
else: result = 'Ошибка ввода'  
print(f'Результат: {result}') 