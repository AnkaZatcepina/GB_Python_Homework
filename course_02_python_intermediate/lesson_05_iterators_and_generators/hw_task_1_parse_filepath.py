"""
    Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. 
    Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""
def parse_filefath(path: str) ->(str,str,str):
    path, ext = path.rsplit('.', 1)
    path, name = path.rsplit('/', 1)
    return (path, name, ext)

print(parse_filefath('/path1/path2/path3/name.exe'))