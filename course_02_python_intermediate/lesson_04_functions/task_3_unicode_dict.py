"""
    ✔ Функция получает на вход строку из двух чисел через пробел.
    ✔ Сформируйте словарь, где ключом будет
    символ из Unicode, а значением — целое число.
    ✔ Диапазон пар ключ-значение от наименьшего из введённых
    пользователем чисел до наибольшего включительно.
"""


def create_unicode_dict(inp_str: str) -> dict[str: int]:
    uni_dict = {}
    a, b = map(int, inp_str.split())
    if a > b:
        a, b = b, a
    for i in range(a,b+1):
        uni_dict[chr(i)] = i
    
    return uni_dict 

print(create_unicode_dict('198 100'))    