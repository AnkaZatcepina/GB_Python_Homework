"""
📌 Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV.
"""

__all__ = ['json_to_csv']

import json
import csv

def json_to_csv(path_json:str, path_csv:str):
    with open(path_json, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    rows = []
    for access_level, users in data.items():
        for ind, name in users.items():
            rows.append({'access_level': int(access_level), 'id': int(ind), 'name': name})
    with open(path_csv, 'w', encoding='utf-8') as csv_file:
        csv_dict = csv.DictWriter(csv_file, fieldnames=['access_level','id','name'],dialect='excel') 
        csv_dict.writeheader()
        csv_dict.writerows(rows)   

if __name__ == '__main__':
    json_to_csv('task_2_file.json','task_3_file.csv') 
              