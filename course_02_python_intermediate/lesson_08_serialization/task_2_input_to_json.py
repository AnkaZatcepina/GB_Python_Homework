"""
📌 Напишите функцию, которая в бесконечном цикле
запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7).
📌 После каждого ввода добавляйте новую информацию в
JSON файл.
📌 Пользователи группируются по уровню доступа.
📌 Идентификатор пользователя выступает ключём для имени.
📌 Убедитесь, что все идентификаторы уникальны независимо
от уровня доступа.
📌 При перезапуске функции уже записанные в файл данные
должны сохраняться.
"""
import os
import json

def input_to_json(path_json:str) -> None:
    user_ids = set()
    if os.path.exists(path_json):
        with open(path_json, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            for user in data.values():
                user_ids.update(user.keys())
    else:
        data = {str(access_level): dict() for access_level in range(1,8)}

    while True:
        name = input('Введите имя: ')
        if not name:
            break
        ind = input('Введите ID: ')
        access_level = input('Введите уровень доступа: ')
        print(f'{ind=} {user_ids=}')
        if ind in user_ids:
            continue
        data[access_level][ind] = name
        with open(path_json, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    input_to_json('task_2_file.json')             