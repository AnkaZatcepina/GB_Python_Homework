"""
    ✔ Напишите программу, которая получает целое число и возвращает
    его двоичное, восьмеричное строковое представление.
    ✔ Функции bin и oct используйте для проверки своего
    результата, а не для решения.
"""
BINARY_DIVIDER: int = 2
OCT_DIVIDER: int = 8

def convert_value(value: int, divider: int) -> str:
    result: str = ''
    while value > 0:
        result = str(value % divider) + result
        value //= divider
    return result  


value: int = int(input('Введите целое число:'))

print(f'Двоичное предствление = {convert_value(value, BINARY_DIVIDER)}')
print(f'Восьмеричное предствление = {convert_value(value, OCT_DIVIDER)}')
print("Проверка:")
print(f'bin(value) = {bin(value)}')
print(f'oct(value) = {oct(value)}')