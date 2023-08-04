"""
Напишите функцию, которая получает на вход директорию и рекурсивно
обходит её и все вложенные директории. Результаты обхода сохраните в
файлы json, csv и pickle.
    ○ Для дочерних объектов указывайте родительскую директорию.
    ○ Для каждого объекта укажите файл это или директория.
    ○ Для файлов сохраните его размер в байтах, а для директорий размер
    файлов в ней с учётом всех вложенных файлов и директорий.
"""

__all__ = ['get_dirsize', 'dir_to_files']

import os
import json
import csv
import pickle

def get_parent_name(path:str, root:str)->str:
    return path[len(root)+1:]

def get_dirsize(path:str)->int:
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size           

def dir_to_files(path:str)->None:
    data = []
    items = os.walk(path)
    for dirpath, dirnames, filenames in os.walk(path):
        for dirname in dirnames:
            dirdata = {}
            dirdata['name'] = dirname
            if dirpath != path:
                dirdata['parent'] = get_parent_name(dirpath,path)
            dirdata['type'] = 'Directory'    
            dirdata['size'] = get_dirsize(f'{dirpath}/{dirname}') 
            data.append(dirdata)
        for filename in filenames:
            filedata = {}
            filedata['name'] = filename
            if dirpath != path:
                filedata['parent'] = get_parent_name(dirpath,path)
            filedata['type'] = 'File'    
            filedata['size'] = os.path.getsize(f'{dirpath}/{filename}')  
            data.append(filedata)  
    
    print(data)   
    with open(f'{path}/result.json', mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=2)     

    with open(f'{path}/result.csv', mode='w', encoding='utf-8') as csv_file:
        csv_writer = csv.DictWriter(csv_file, dialect='excel', quoting=csv.QUOTE_NONNUMERIC, 
                                    fieldnames=['name','parent','type','size'],
                                    restval="-")
        csv_writer.writeheader()
        csv_writer.writerows(data)

    with open(f'{path}/result.pickle', mode='wb') as pickle_file:
        pickle.dump(data, pickle_file)    

if __name__ == '__main__':
   dir_to_files('./hw_task_1_folder') 