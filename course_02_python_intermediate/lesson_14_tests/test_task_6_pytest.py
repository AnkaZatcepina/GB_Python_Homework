"""
    📌 На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
    📌 Напишите 3-7 тестов pytest для данного проекта.
    📌 Используйте фикстуры.
"""

import sys
import pathlib
if __package__ is None:                  
    DIR = pathlib.Path(__file__).resolve().parent
    sys.path.insert(0, str(DIR.parent))
    __package__ = DIR.name


from typing import Set
from lesson_13_exceptions.task_4_access_level import User
from lesson_13_exceptions.task_5_project import Project
import pytest  

@pytest.fixture
def new_set() -> Set[User]:
    user_set = {User('Bob', 1, 7), 
                User('John', 2, 4),
                User('Jane', 3, 2)}
    return user_set

def test_entrance(new_set):
    project = Project('task_6_file.json')
    result = project.get_users_from_json('task_6_file.json')
    assert result == new_set

if __name__ == '__main__':
    pytest.main(['-vv'])      