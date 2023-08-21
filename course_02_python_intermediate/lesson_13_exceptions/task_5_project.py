"""
    📌 Доработаем задачи 3 и 4. Создайте класс проекта, который
    имеет следующие методы:
    📌 загрузка данных (функция из задания 4)
    📌 вход в систему - требует указать имя и id пользователя. Для
    проверки наличия пользователя в множестве используйте
    магический метод проверки на равенство пользователей.
    Если такого пользователя нет, вызывайте исключение
    доступа. А если пользователь есть, получите его уровень из
    множества пользователей.
    📌 добавление пользователя. Если уровень пользователя
    меньше, чем ваш уровень, вызывайте исключение уровня
    доступа.
"""
import sys
import pathlib
if __package__ is None:                  
    DIR = pathlib.Path(__file__).resolve().parent
    sys.path.insert(0, str(DIR.parent))
    __package__ = DIR.name

import json
from typing import Set
from task_4_access_level import User
from task_3_class import AccessException, LevelException

class Project:
    def __init__(self, path_json:str):
        self.admin_user = None
        self.path_json = path_json
        self.users = self.get_users_from_json(self.path_json)

    def get_users_from_json(self, path_json:str) -> Set[User]:
        with open(path_json, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        user_set = set()
        for access_level, users in data.items():
            for ind, name in users.items():
                user_set.add(User(name,int(ind),int(access_level)))
        return user_set  

    def entrance(self, name: str, user_id: int):
        test_user = User(name, user_id, 0)
        if test_user in self.users:
            for user in self.users:
                if test_user == user:
                    self.admin_user = user
                    return self.admin_user.access_level
        else:
            raise AccessException(name, user_id)  

    def add_user(self, name: str, user_id: int, access_level: int):
        if access_level > self.admin_user.access_level:
            raise LevelException(self.admin_user, access_level) 
        new_user = User(name, user_id, access_level) 
        self.users.add(new_user)

if __name__ == '__main__':
    my_project = Project('task_4_file.json')
    print(my_project.entrance("Толик", 1))
    my_project.add_user("Новый_1", 333, 1) 
    print(*my_project.users, sep='\n')
    my_project.add_user("Новый_2", 333, 5)            
