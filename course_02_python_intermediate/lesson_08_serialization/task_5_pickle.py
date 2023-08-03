"""
    Напишите функцию, которая ищет json файлы в указанной
    директории и сохраняет их содержимое в виде
    одноимённых pickle файлов.
"""
import json
import pickle
import os

def files_to_pickle(path: str)->None:
    json_files = filter(lambda file_name: file_name[-5::] == '.json', os.listdir())
    for json_file in json_files:
        with open(json_file, 'r', encoding='utf-8') as json_reader:
            data = json.load(json_reader)
        with open(f'{json_file[:-5]}.pickle', 'wb') as pickle_writer:
            pickle.dump(data, pickle_writer)

if __name__ == '__main__':
    files_to_pickle('.') 