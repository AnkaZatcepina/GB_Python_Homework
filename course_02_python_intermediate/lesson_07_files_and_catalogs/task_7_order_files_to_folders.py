"""
    ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
    ✔ Каждая группа включает файлы с несколькими расширениями.
    ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""

__all__ = ['create_folders', 'order_files']

import os

file_folders = {
    'video': ('mkv', 'mp4', 'avi'),
    'image': ('jpeg', 'jpg', 'img'),
    'text': ('txt', 'doc'),
}

def create_folders()->None:
    for folder in file_folders.keys():
        if not os.path.exists(folder):
            os.mkdir(folder)

def order_files(dir: str = 'task_7_files')->None:
    os.chdir(dir)
    create_folders()
    files = os.scandir()
    for file in files:
        if not os.path.isfile(file):
            continue
        filepath = file.path
        ext = filepath.split('.')[-1]
        filename = filepath.split('/')[-1]
        for folder, exts in file_folders.items():
            if ext in exts:
                print(f'Файл {filename} перемещён в папку {folder}' )
                os.replace(filename, os.path.join(folder, filename))

if __name__ == '__main__':
    order_files()                    