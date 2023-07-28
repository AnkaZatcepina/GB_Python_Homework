"""
    ✔ Дорабатываем функции из предыдущих задач.
    ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
    ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
    (добавьте проверки).
    ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
"""
__all__ = ['gen_name', 'check_dir', 'create_files', 'create_files_many_ext']

from random import choices, randint
from string import ascii_lowercase, digits
import os

def gen_name(min_name: int, max_name: int) -> str:
    return ''.join(choices(ascii_lowercase+digits+'_', k=randint(min_name, max_name)))

def check_dir(dir:str, **kwargs)->None:
    if not os.path.exists(dir):
        os.mkdir(dir)
    os.chdir(dir)  
    create_files_many_ext(**kwargs)

def create_files(extension: str, 
                min_name: int = 6, max_name: int = 30,
                min_bytes: int = 256, max_bytes: int = 4096,
                amount: int = 42) -> None:
    for _ in range(amount):
        name = gen_name(min_name, max_name)
        my_bytes = bytes(randint(0,255) for _ in range(randint(min_bytes, max_bytes)))
        with open(rf'{name}.{extension}', 'wb') as file:
            file.write(my_bytes)

def create_files_many_ext(**kwargs):
    for ext, amount in kwargs.items():
        create_files(ext, amount = amount)        

if __name__ == '__main__':
    check_dir('task_6_files', txt=2,xml=1)