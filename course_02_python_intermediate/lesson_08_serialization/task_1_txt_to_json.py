"""
    📌 Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
    текстовый файл с псевдо именами и произведением чисел.
    📌 Напишите функцию, которая создаёт из созданного ранее
    файла новый с данными в формате JSON.
    📌 Имена пишите с большой буквы.
    📌 Каждую пару сохраняйте с новой строки.
"""

import json

def txt_to_json(path_file_txt: str, path_file_json: str) -> None:
    file_dict = {}
    with open(path_file_txt, mode='r', encoding='utf-8') as file_txt:
        for line in file_txt:
            name, numb = line.split('|')
            file_dict[name.capitalize()] = float(numb)

    with open(path_file_json, mode='w',encoding='utf-8') as file_json:
        json.dump(file_dict, file_json, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    txt_to_json('task_1_file.txt', 'task_1_file.json')       

