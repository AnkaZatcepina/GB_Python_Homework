"""
    Напишите функцию группового переименования файлов. Она должна:
        ✔ принимать параметр желаемое конечное имя файлов.
        При переименовании в конце имени добавляется порядковый номер.
        ✔ принимать параметр количество цифр в порядковом номере.
        ✔ принимать параметр расширение исходного файла.
        Переименование должно работать только для этих файлов внутри каталога.
        ✔ принимать параметр расширение конечного файла.
        ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
        [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
        желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
"""

__all__ = ['rename_files', ]

import os
  
def rename_files(desired_filename: str, 
                index_len: int, 
                old_ext: str, 
                new_ext: str, 
                slicer: slice,
                dir: str = 'hw_task_1_files') -> None:
    os.chdir(dir)
    index = 0
    files = os.scandir()
    for file in files:
        if not os.path.isfile(file):
            continue 
        filepath = file.path
        ext = filepath.split('.')[-1]
        filename = filepath.split('/')[-1]
        if ext != old_ext:
            continue 
        index += 1
        new_filename = \
            f'{filename[slicer]}'\
            f'{desired_filename if desired_filename else ""}'\
            f'{index:0{index_len}d}'\
            f'.{new_ext}'
            
        print(f'Файл {filename} переименован в {new_filename}' )
        os.rename(filename, new_filename)

if __name__ == '__main__':
    rename_files(desired_filename='_new_', index_len=4, old_ext='txt', new_ext='doc', slicer=slice(0, 3, None)) 
