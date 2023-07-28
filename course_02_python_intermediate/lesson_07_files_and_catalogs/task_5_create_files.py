"""
    ✔ Доработаем предыдущую задачу.
    ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
    ✔ Расширения и количество файлов функция принимает в качестве параметров.
    ✔ Количество переданных расширений может быть любым.
    ✔ Количество файлов для каждого расширения различно.
    ✔ Внутри используйте вызов функции из прошлой задачи.
"""

from random import choices, randint
from string import ascii_lowercase, digits

def gen_name(min_name: int, max_name: int) -> str:
    return ''.join(choices(ascii_lowercase+digits+'_', k=randint(min_name, max_name)))

def create_files(extension: str, 
                min_name: int = 6, max_name: int = 30,
                min_bytes: int = 256, max_bytes: int = 4096,
                amount: int = 42) -> None:
    for _ in range(amount):
        name = gen_name(min_name, max_name)
        my_bytes = bytes(randint(0,255) for _ in range(randint(min_bytes, max_bytes)))
        with open(rf'task_4_files/{name}.{extension}', 'wb') as file:
            file.write(my_bytes)

def create_files_many_ext(**kwargs):
    for ext, amount in kwargs.items():
        create_files(ext, amount = amount)        

if __name__ == '__main__':
    create_files_many_ext(txt=3,jpeg=2)