"""
    ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
    Функция принимает следующие параметры:
        ✔ расширение
        ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
        ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
        ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
        ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
        ✔ количество файлов, по умолчанию 42
    ✔ Имя файла и его размер должны быть в рамках переданного диапазона.
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

if __name__ == '__main__':
     create_files('txt', amount=2) 