"""
    📌 Прочитайте созданный в прошлом задании csv файл без
    использования csv.DictReader.
    📌 Дополните id до 10 цифр незначащими нулями.
    📌 В именах первую букву сделайте прописной.
    📌 Добавьте поле хеш на основе имени и идентификатора.
    📌 Получившиеся записи сохраните в json файл, где каждая строка
    csv файла представлена как отдельный json словарь.
    📌 Имя исходного и конечного файлов передавайте как аргументы
    функции.
"""

import json
import csv

def csv_to_json(path_csv:str, path_json:str):
    with open(path_csv, 'r', encoding='utf-8') as csv_file:
        csv_rows = csv.reader(csv_file, dialect='excel')
        data = []
        for i, row in enumerate(csv_rows):
            if i:
                access_level, user_id, name = row
                user_data = {}
                user_data['access_level'] = int(access_level)
                user_data['user_id'] = f'{int(user_id):010}'
                user_data['name'] = name.capitalize()                
                user_data['hash'] = hash((user_id,name))
                data.append(user_data)
    
    with open(path_json, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file,ensure_ascii=False,indent=2) 

if __name__ == '__main__':
    csv_to_json('task_3_file.csv','task_4_file.json') 