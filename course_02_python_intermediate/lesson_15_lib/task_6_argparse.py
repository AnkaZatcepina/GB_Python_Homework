"""
📌 Напишите код, который запускается из командной строки и получает на вход
путь до директории на ПК.
📌 Соберите информацию о содержимом в виде объектов namedtuple.
📌 Каждый объект хранит:
    ○ имя файла без расширения или название каталога,
    ○ расширение, если это файл,
    ○ флаг каталога,
    ○ название родительского каталога.
📌 В процессе сбора сохраните данные в текстовый файл используя
логирование.
"""

from pathlib import Path
import argparse
from collections import namedtuple
import logging

logging.basicConfig(filename='task_6.log', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

File = namedtuple('File', 'name, extension, is_dir, parent_dir')

def read_dir(path:Path):
    for file in path.iterdir():
        f = File(file.stem if file.is_file() else file.name, 
                file.suffix, 
                file.is_dir(), 
                file.parent)
        logger.info(f)
        if f.is_dir:
            read_dir(Path(f.parent_dir)/f.name)

if __name__ == '__main__':
    print(Path.cwd())
    read_dir(Path('/config/workspace/python/GB/python_homework/course_02_python_intermediate'))
