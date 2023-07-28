"""
    ✔ Напишите функцию, которая открывает на чтение созданные
    в прошлых задачах файлы с числами и именами.
    ✔ Перемножьте пары чисел. В новый файл сохраните
    имя и произведение:
        ✔ если результат умножения отрицательный, сохраните имя
    записанное строчными буквами и произведение по модулю
        ✔ если результат умножения положительный, сохраните имя
    прописными буквами и произведение округлённое до целого.
    ✔ В результирующем файле должно быть столько же строк,
    сколько в более длинном файле.
    ✔ При достижении конца более короткого файла,
    возвращайтесь в его начало.
"""
from typing import TextIO

def readline_or_begin(file: TextIO) -> str:
    text = file.readline()
    if text == '':
        file.seek(0)
        text = file.readline()
    return text[:-1]  


def combine_2_files(filename_numbs: str = 'task_1_file.txt', 
                    filename_names: str = 'task_2_file.txt',
                    filename_result: str = 'task_3_file.txt'):
    with open(filename_numbs, encoding='utf-8') as file_numbs, \
         open(filename_names, encoding='utf-8') as file_names, \
         open(filename_result, 'w', encoding='utf-8') as file_result:

        len_numbs = len(file_numbs.readlines())
        len_names = len(file_names.readlines())

        for _ in range(max(len_numbs,len_names)):
            
            numb = readline_or_begin(file_numbs)
            name = readline_or_begin(file_names)   
            a, b = numb.split("|")
            mult = int(a) * float(b)
            if mult > 0:
                file_result.write(name.upper() + '|' + str(round(mult)) + '\n')
            else:
                file_result.write(name.lower() + '|' + str(-mult) + '\n')   


if __name__ == '__main__':
    combine_2_files()            