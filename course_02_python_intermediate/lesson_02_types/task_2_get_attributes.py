"""
    Создайте в переменной data список значений разных типов перечислив их через
    запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
    ✔ порядковый номер начиная с единицы
    ✔ значение
    ✔ адрес в памяти
    ✔ размер в памяти
    ✔ хэш объекта
    ✔ результат проверки на целое число только если он положительный
    ✔ результат проверки на строку только если он положительный
    Добавьте в список повторяющиеся элементы и сравните на результаты.
"""
import sys

data = [1, 45, 'text', 2.12, False]
for i,item in enumerate(data):
    adress: int = id(item)
    size_item: int = sys.getsizeof(item)
    hash_item: int = hash(item)
    result: str = ''
#    if isinstance(item, int):
    if type(item)==int:
        result = ', Это целое число'
    elif isinstance(item, str):   
        result = ', Это строка'
    print(f'Номер: {i}, значение: {item}, адрес: {adress},' 
        f' размер: {size_item}, хэш: {hash_item}{result}')
