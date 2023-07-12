"""
    Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
    hex используйте для проверки своего результата.
"""
HEX_DIVIDER: int = 16
HEX_DICT: str = '0123456789ABCDEF'

def convert_value(value: int) -> str:
    result: str = ''
    while value > 0:
        result = HEX_DICT[value % HEX_DIVIDER] + result
        value //= HEX_DIVIDER
    return result  


value: int = int(input('Введите целое число:'))
print(f'Шестнадцатеричное предствление = {convert_value(value)}')
print(f'Проверка: hex(value) = {hex(value)}')
