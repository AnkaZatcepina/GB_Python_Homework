"""
    Пользователь вводит данные. Сделайте проверку данных
    и преобразуйте если возможно в один из вариантов ниже:
    ✔ Целое положительное число
    ✔ Вещественное положительное или отрицательное число
    ✔ Строку в нижнем регистре, если в строке есть
    хотя бы одна заглавная буква
    ✔ Строку в верхнем регистре в остальных случаях
"""


input_str = input(f'Введите строку: ')
result = ''

if (input_str.count('-')==0) and input_str.isdecimal():
    result = int(input_str)

elif input_str[1:].count('-') == 0 \
    and input_str.count('.')  <= 1 \
    and input_str.replace('.', '', 1).replace('-', '', 1).isdecimal():
    result = float(input_str)

elif not input_str.islower():
    result = input_str.lower()
    
else:
    result = input_str.upper()  

print(type(result),result)