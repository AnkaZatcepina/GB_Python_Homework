"""
    📌 Вспоминаем задачу из семинара 8 про сериализацию данных,
    где в бесконечном цикле запрашивали имя, личный
    идентификатор и уровень доступа (от 1 до 7) сохраняя
    информацию в JSON файл.
    📌 Напишите класс пользователя, который хранит эти данные в
    свойствах экземпляра.
    📌 Отдельно напишите функцию, которая считывает информацию
    из JSON файла и формирует множество пользователей.
"""

import json
from typing import Set

class User:
    def __init__(self, name: str, user_id: int, access_level: int):
        self.name = name
        self.user_id = user_id
        self.access_level = access_level

    def __eq__(self,other):
        return self.user_id == other.user_id and self.name == self.name

    def __hash__(self):
        return hash((self.user_id, self.name))

    def __str__(self) -> str:
        return f'{self.name}, {self.user_id}, {self.access_level}'    

def get_users_from_json(path_json:str) -> Set[User]:
    with open(path_json, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    user_set = set()
    for access_level, users in data.items():
        for ind, name in users.items():
            user_set.add(User(name,ind,access_level))
    return user_set   

if __name__ == '__main__':
    print(list(str(user) for user in get_users_from_json('task_4_file.json')))
    print(*get_users_from_json('task_4_file.json'), sep='\n')