"""
    📌 Напишите функцию, которая преобразует pickle файл
    хранящий список словарей в табличный csv файл.
    📌 Для тестированию возьмите pickle версию файла из задачи
    4 этого семинара.
    📌 Функция должна извлекать ключи словаря для заголовков
    столбца из переданного файла.
"""

__all__ = ['pickle_to_csv']

import pickle
import csv

def pickle_to_csv(path_pickle: str, path_csv: str)->None:
    with open(path_pickle,'rb') as pickle_file:
        data = pickle.load(pickle_file)
    headers = data[0].keys()
    with open(path_csv,'w',encoding='utf-8') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=headers, dialect='excel', 
                                    quoting=csv.QUOTE_NONNUMERIC)   
        csv_writer.writeheader()
        csv_writer.writerows(data)

if __name__ == '__main__':
    pickle_to_csv('task_4_file.pickle','task_6_file.csv') 